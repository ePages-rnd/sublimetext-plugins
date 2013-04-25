import sublime_plugin

class RunBuildCvsCommand(sublime_plugin.WindowCommand):
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

class QuickCvsCommitBuildTargetCommand(sublime_plugin.WindowCommand):
    def run(self, cmd = [], file_regex = "", line_regex = "", working_dir = "", encoding = "utf-8", env = {}, path = "", shell = False):
        self.execDict = {
            "path" : path,
            "shell" : shell,
            "cmd" : cmd,
            "file_regex" : file_regex,
            "line_regex" : line_regex,
            "working_dir" : working_dir,
            "encoding" : encoding,
            "env" : env
        }
        self.window.show_input_panel("Commit message", "\"" + self.execDict["cmd"][3] + ":\"", self.on_done, None, None)
    def on_done(self, message):
        self.execDict["cmd"][3] = message
        self.window.run_command('exec', self.execDict)