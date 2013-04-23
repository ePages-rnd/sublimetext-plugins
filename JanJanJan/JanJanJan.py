import sublime, sublime_plugin
import re

class RunBuildCommand(sublime_plugin.WindowCommand):
    # helper 
    #  * for setting the build_system
    #  * running build
    #  * and then resetting the build_system to automatic
    def run(self, build_system, build_variant):  
        self.window.run_command( "set_build_system", {"file": build_system } )
        self.window.run_command( "build", {
            "variant": build_variant
        })
        self.window.run_command("set_build_system", {"file":""}) # Set build_system to *automatic*
        
class ChooseVmCommand(sublime_plugin.WindowCommand):
    # Choose virtual machine according to "vms" array
    # in "JanJanJan.sublime-settings".
    # Then, pass *command* and *args* to
    # *run_command_with_vm* or *exec_command_on_vm*
    def run(self, command, args={}, runcommand=False):
        self.command = command
        self.args = args
        self.runcommand = runcommand
        self.window.show_quick_panel(sublime.load_settings("JanJanJan.sublime-settings").get("vms"), self.on_done, sublime.MONOSPACE_FONT)
    def on_done(self, index):
        if index > -1:
            self.window.run_command("run_command_with_vm" if self.runcommand else "exec_command_on_vm", {
                "command":self.command, 
                "vm":sublime.load_settings("JanJanJan.sublime-settings").get("vms")[index][0],
                "args":self.args
            })

class ExecFileCommandOnVmCommand(sublime_plugin.WindowCommand):
    # Executes a *command* defined in "JanJanJan.sublime-settings" 
    # under the *file_commands* key on the given virtual machine via ssh
    # appending the filepath to the command
    def run(self, command, args={}):
        filepath_to_vm = sublime.load_settings("JanJanJan.sublime-settings").get("filepath_to_vm")
        m = re.compile(filepath_to_vm).match(self.window.active_view().file_name())
        filepath_to_eproot = sublime.load_settings("JanJanJan.sublime-settings").get("filepath_to_eproot")
        n = re.compile(filepath_to_eproot).match(self.window.active_view().file_name())
        if m:
            if n:
                fileCommands = sublime.load_settings("JanJanJan.sublime-settings").get("file_commands", {})
                if fileCommands[command]:
                    sshSettings = sublime.load_settings("JanJanJan.sublime-settings").get("ssh", {
                        "command" : "ssh",
                        "path" : "/usr/bin"
                    })
                    cmd = []
                    if sshSettings["command"]:
                        cmd.append(sshSettings["command"])
                    else:
                        cmd.append("ssh")
                    cmd.append("root@" + m.group(1))
                    cmd.append(fileCommands[command]["cmd"] + " /srv/epages/eproot/" + n.group(1))
                    if sshSettings["path"]:
                        self.window.run_command("exec",{
                            "cmd" : cmd,
                            "path" : sshSettings["path"]
                        })
                    else:
                        self.window.run_command("exec",{
                            "cmd" : cmd
                        })
                else:
                    sublime.error_message("Cannot find file_command " + command + "in JanJanJan settings.")
            else:
                sublime.error_message("Cannot guess filepath (relative to the virtual machine) from: " + self.window.active_view().file_name())
        else:
            sublime.error_message("Cannot guess virtual machine from: " + self.window.active_view().file_name())

class ExecCommandOnVmCommand(sublime_plugin.WindowCommand):
    # Executes a *command* defined in "JanJanJan.sublime-settings" 
    # under the *commands* key on the given virtual machine via ssh.
    def run(self, command, args={}, vm=""):
        if vm:
            if sublime.platform() == "windows":
                if vm == "C":
                    windowsCommands = sublime.load_settings("JanJanJan.sublime-settings").get("windows_commands", {})
                    self.window.run_command("exec",{
                        "cmd" : windowsCommands[command]["cmd"]
                    })
                else:
                    vmName = sublime.load_settings("JanJanJan.sublime-settings").get("drive_letter_to_vm_name", {})[vm]
                    pathToPutty = sublime.load_settings("JanJanJan.sublime-settings").get("path_to_putty")
                    self.window.run_command('exec',{
                        'cmd':[pathToPutty, '-load', vmName, '-m', sublime.packages_path() + '\\JanJanJan\\' + command + '.sh']
                    })
            else:    
                vmCommands = sublime.load_settings("JanJanJan.sublime-settings").get("commands", {})
                if vmCommands[command]:
                    sshSettings = sublime.load_settings("JanJanJan.sublime-settings").get("ssh", {
                        "command" : "ssh",
                        "path" : "/usr/bin"
                    })
                    cmd = []
                    if sshSettings["command"]:
                        cmd.append(sshSettings["command"])
                    else:
                        cmd.append("ssh")
                    cmd.append("root@" + vm)
                    cmd.append(vmCommands[command]["cmd"])
                    if sshSettings["path"]:
                        self.window.run_command("exec",{
                            "cmd" : cmd,
                            "path" : sshSettings["path"]
                        })
                    else:
                        self.window.run_command("exec",{
                            "cmd" : cmd
                        })
        else:
            filepath_to_vm = sublime.load_settings("JanJanJan.sublime-settings").get("filepath_to_vm")
            m = re.compile(filepath_to_vm).match(self.window.active_view().file_name())
            if m:
                self.run(command, args, m.group(1))
            else:
                self.window.run_command("choose_vm", {"command":command, "args":args})

class RunCommandWithVmCommand(sublime_plugin.WindowCommand):
    # Adapter for running window commands
    # which need a virtual machine to run with (e.g. "open error log").
    # If the *vm* parameter is empty, *choose_vm*
    # will be run to find a *vm*.
    def run(self, command, args={}, vm=""):
        if vm:
            self.window.run_command(command + '_on_vm', {"vm": vm, "args" : args})
        else:
            filepath_to_vm = sublime.load_settings("JanJanJan.sublime-settings").get("filepath_to_vm")
            m = re.compile(filepath_to_vm).match(self.window.active_view().file_name())
            if m:
                self.run(command, args, m.group(1))
            else:
                self.window.run_command("choose_vm", {"command":command, "args":args, "runcommand":True})

class OpenFileOnVmCommand(sublime_plugin.WindowCommand):
    def run(self, vm, template_string="", args={}):
        self.vm=vm
        if template_string:
            self.on_done(template_string)
        else:
            self.window.show_input_panel("Paste it, baby!", "", self.on_done, None, None)

    def on_done(self, template_string):
        filename = self.window.active_view().file_name()
        m = re.compile(r"^.*[\\|/](Cartridges.*?) .*$").match(template_string + " ")
        vm = self.vm
        path = ""
        if m:
            path = sublime.load_settings("JanJanJan.sublime-settings").get(vm, "/Volumes/" + vm + "/srv/epages/eproot/") + m.group(1)
        else:
            m = re.compile(r"^.*[\\|/](WebRoot.*?) .*$").match(template_string + " ")
            if m:
                path = sublime.load_settings("JanJanJan.sublime-settings").get(vm, "/Volumes/" + vm + "/srv/epages/eproot/") + "Shared/" + m.group(1)
        if (sublime.platform() == "windows"):
            path = re.sub("/", r"\\", path)
        else:
            path = re.sub(r"\\", "/", path)
        if path:
            self.window.open_file(path)
        else:
            sublime.error_message("Cannnot guess epages filename from " + template_string)


class OpenFileFromClipboardOnVmCommand(sublime_plugin.WindowCommand):
    def run(self, vm, args={}):
        self.window.run_command("open_file_on_vm", {
            "template_string" : sublime.get_clipboard(),
            "vm" : vm
        })

class OpenLogOnVmCommand(sublime_plugin.WindowCommand):
    def run(self, vm, args):
        path = sublime.load_settings("JanJanJan.sublime-settings").get(vm, "/Volumes/" + vm + "/srv/epages/eproot/") + "Shared/Log/" + args["name"] + ".log"
        if (sublime.platform() == "windows"):
            path = re.sub("/", r"\\", path)
        else:
            path = re.sub(r"\\", "/", path)
        if path:
            self.window.open_file(path)