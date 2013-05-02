sublimetext-plugins
=================

[Sublime Text 2](http://www.sublimetext.com/2) plugins that may allow you to have a better workflow.

---

- [Installation](#installation)
- [Configuration](#configuration)
- [Plugins](#plugins)
  - [Flakes](#flakes)
  - [QuickCVS](#quickcvs)
- [Notes on Development](#development)

Installation
------------
The plugins are available through [Sublime Package Contol](http://wbond.net/sublime_packages/package_control). Each plugin has its own repo. This repo is only the interface, which gathers the plugins in place.

So you have to install Package Control first, if you haven't done this yet:

* Click the **View > Show Console** menu entry.
* Copy and paste following right into the console: ```import urllib2,os; pf='Package Control.sublime-package'; ipp=sublime.installed_packages_path(); os.makedirs(ipp) if not os.path.exists(ipp) else None; urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler())); open(os.path.join(ipp,pf),'wb').write(urllib2.urlopen('http://sublime.wbond.net/'+pf.replace(' ','%20')).read()); print('Please restart Sublime Text to finish installation')```
* Hit return.
* Restart Sublime Text 2.

Our plugin resides at this repo, so you have to add the URL manually:

* Click on **Preferences > Package Settings > Package Control > Settings - User**.
* Copy & paste following snippet into this file: ```
{
    "auto\_upgrade\_frequency": 0,
    "repository_channels":
    [
        "https://raw.github.com/jgratz4epages/sublimetext-plugins/master/repositories.json"
    ],
    "submit_usage": false
}```
* Save the file and restart Sublime.

Now you can install the two plugins:

* Hit **Ctrl-Shift-P** or **Cmd-Shift-P** and choose **QuickCVS**.
* Repeat for **Flakes**.
* Repeat for CTags and FileDiff as well, they're very helpful plugins, too.

Configuration
--------------
See the **README.md** inside the plugin folders for personal settings you may have to adjust.

Plugins
--------
### [Flakes](https://github.com/ePages-rnd/sublimetext-epages-flakes)
Basic functionality for working with virtual machines running epages on unix and windows, e.g.

* Open file (e.g. copy template debugging comment -> strg+shift+o in Sublime Text -> opens file on your system).
* Restart app server.
* Restart perl.
* Set JSDebugLevel.
* Import and delete XMLs.
* Import and delete hook XMLs.
* Perl::Critic.
* Perl syntax check.
* Javascript syntax check.
* Perl organize imports.
* Correct permissions.
* Ctags perl (Linux only, requires ctags plugin).
* ...

### [QuickCVS](https://github.com/ePages-rnd/sublimetext-quickcvs)
Runs **cvs** on your console and prints output to Sublime Text 2 console.

* Status
* Diff
* Update
* Get Clean Copy
* Commit

Development
----------
* Resources for development:
  * [Sublime Info - Information about Sublime Text 2](http://sublimetext.info/)
