JanJanJan
=================

[Sublime Text 2](http://www.sublimetext.com/2) plugin that helps... a lot!...

---

- [Installation](#installation)
- [Configuration](#configuration)
  - [Windows](#windows)
  - [Unix](#unix)


Installation
------------
Manually copy the **JanJanJan** folder inside this repository to your Packages directory. In Sublime Text:

* Click the **Preferences > Browse Packages…** menu entry.
* Browse up a folder. You should see a **Packages** directory.
* Download the desired folder from this repo and copy it into the **Packages** directory
* Restart Sublime Text

Configuration
--------------
Edit User Settings:
* In Sublime Text. 
* Click the **Preferences > Package Settings > JanJanJan > User - Settings User** menu entry.
* Edit the following **json** object and save it into your User Settings file.
### Windows
``` js
{
    "C": "C:/epages/", // "driveletter" : "Path to eproot on that drive"
    "X": "X:/", // You can add more virtual machines mounted on more drives here.
    "vms": [
        [
            "C", "Lokal" // "driveletter" : "Description of the machine mounted on the driveletter"
        ],
    
        [
            "X", "VM1" // You can add more virtual machines mounted on more drives here.
        ]
    ],
    "drive_letter_to_vm_name" : {
    	"X" : "myname-vm-lin-1" // "driveletter" : "name of the virtual machine on the nextwork"
    },
    "path_to_putty" : "C:\\Users\\username\\Downloads\\putty" // Place the path to your putty folder here.
}
```
### Unix
``` js
{
  "jr-vm-lin-1" : "/Volumes/jr-vm-lin-1/srv/epages/eproot/", 
  // "hostname of virtual machine" : "path to eproot on virtual machine on your file system"
  "jr-vm-lin-2" : "/Volumes/jr-vm-lin-2/srv/epages/eproot/",
  "jr-vm-lin-3" : "/Volumes/jr-vm-lin-3/srv/epages/eproot/",
  "vms" : [
    ["jr-vm-lin-1", "VM1"],
  // ["hostname of virtual machine", "Some description"]
    ["jr-vm-lin-2", "VM2"],
    ["jr-vm-lin-3", "VM3"]
  ],
  "filepath_to_vm" : "\\/Volumes\\/(.*)\\/srv\\/epages\\/.*$",
  // regex matching a filepath to the hostname of a virtual machine
  "filepath_to_eproot" : "\\/Volumes\\/.*\\/srv\\/epages\\/eproot/(.*)$", // used for ExecFileCommandOnVmCommand
  // regex matching a filepath to a relative filepath, i.e. relative to eproot.
}
```


