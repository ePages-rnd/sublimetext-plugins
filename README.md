sublimetext-plugins
=================

[Sublime Text 2](http://www.sublimetext.com/2) plugins that may allow you to have a better workflow.

---

- [Installation](#installation)
- [Configuration](#configuration)
- [Plugins](#plugins)
  - [JanJanJan](#janjanjan)
  - [Epages](#epages)
- [Notes on Development](#development)

Installation
------------
Currently the plugins are **not** available through [Sublime Package Contol](http://wbond.net/sublime_packages/package_control). 
So you have to manually copy the desired plugins (i.e. folders in this repository) to your Packages directory. In Sublime Text:

* Click the **Preferences > Browse Packages…** menu entry.
* Browse up a folder. You should see a **Packages** directory.
* Download the desired folder from this repo and copy it into the **Packages** directory
* Restart Sublime Text

Configuration
--------------
See the **README.md** inside the plugin folders for personal settings you may have to adjust.

Plugins
--------
### [JanJanJan](JanJanJan/)
Basic functionality for working with virtual machines running epages on unix and windows, e.g.
* Open file (e.g. copy template debugging comment -> strg+shift+o in Sublime Text -> opens file on your system).
* Restart app server.
* Restart perl.
* Set JSDebugLevel.
* Import and delete XMLs.
* Import and delete hook XMLs.
* Ctags perl (Linux only, requires ctags plugin).
* Perl::Critic.
* Perl syntax check.
* Javascript syntax check.
* Perl organize imports.
* Correct permissions.
* ...

### [Epages](Epages/)
More integrated **cvs** and **task-managment** implementation, e.g.
* Open in CVS GUI
* Log, StackTrace snippet for Perl files
* virtual folders (summarize files to virtual folders/tasks)
* ...

Development
----------
* Try to **avoid duplication** of functionality in different plugins.
* The aim should be to have **all plugins** in this repo working next to each other.
* Document functionality in a **README.md** in your plugin folder.
* Resources for development:
  * [Sublime Info - Information about Sublime Text 2](http://sublimetext.info/)
