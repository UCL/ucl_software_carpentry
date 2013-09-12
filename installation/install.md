# UCL ![Software Carpentry logo](http://software-carpentry.org/img/software-carpentry-banner.png "Software Carpentry logo") Bootcamp Thursday 26th and Friday 27th September, 2013: Installation Instructions #

This document contains instructions for installation of the packages
we'll be using during the Software Carpentry Workshop on the 26th and 27th September, 2013

For the session on programming, we'll be using the language *Python* and in particular version 2.7. We will use the *Enthought Canopy* 
python distribution which contains a good collection of the most common *Python* modules as well as *IPython* 
(an improved *Python* interpreter) and the IPython notebook (a useful web-based user interface that allows
you to create documents that combine text and *Python* code, executable with the same browser window).
We'll need *pip*, the package installer for *Python*, as well.

For the workshop session on version control, 
we'll be using *Git* and the *Github* website.

Linux users should be able to use their package manager to install all of this software
(if you're using Linux, we assume you won't have any trouble with these requirements).
However note that if you are running an older linux distribution you may get older versions with different look and features.
A resent linux distribution is recommended. 

Mac and Windows users should follow the instructions below.

Give yourself 30 minutes or so to run through this installation process and don't get intimidated!
Please try to install everything well before the bootcamp,
as it is important that we don't waste time during the workshop trying to mend installations. 

If you do get stuck, first try searching on the internet (e.g. [stackoverflow.com](http://stackoverflow.com)) for solutions.
Or, try asking a fellow bootcamp attendee for help.


We will be running a drop-in session on the afternoon of Monday 23rd September from 13:00 - 17:00 in Room G07,
Chadwick Building (main campus on Gower Street) for people that would like some help with setting up their laptop in 
advance of the boot camp. There is no need to pre-book for this. All students should either attend this or ensure 
that they have a working git, python, and editor and shell installation by following the instructions bellow. 

## Linux Users ##

### Python ###
There are various ways of installing python and the needed python packages on Linux.

#### Package manager ####

Recent versions of Ubuntu (12.10 and 13.04) pack mostly up to date versions of all needed packages. 
You should ensure that the following packages are installed:

*  python-numpy  
*  python-scipy  
*  python-nose
*  python-matplotlib
*  python-pip
*  ipython
*  ipython-notebook

Older distributions may have outdated versions of specific packages. 
Other linux distributions most likely also contain the needed python packages but 
they may also be outdated. 

#### Enthought Canopy ####

Alternatively we may install a complete independent scientific python distribution. On of these is 
Enthought Canopy. 

The Enthought Canopy python distribution exists in two different versions. A basic free version with a 
limited number of packages (Canopy express) and a non free full version. The full version can be obtained 
free of charge for academic use. Register with [Enthought Scientific Computing](https://enthought.com/products/canopy/academic/)
using your UCL e-mail address for an academic licence.

You may then use your Enthought user account to sign into the installed Canopy application and activate the full academic version. 
Canopy comes with a package manager from where it is possible to install and update a large number of python packages. 
The packages installed by default should cover our needs.

### Git ###

If git is not already available on your machine 
you can try to install it via your distribution package manager (e.g. `apt-get` or `yum`).

### Editor and shell ###

Many different text editors suitable for programming are available.
If you don't already have a favourite,
you could look at [Kate](http://kate-editor.org/).

Regardless of which editor you have chosen you should configure git to use it. Executing something like this in a terminal should work:

```
git config --global core.editor NameofYourEditorHere
```

The default shell is usually bash but if not you can get to bash by opening a terminal and typing `bash`.

## Mac Users ##

### Python ###

#### Enthought Canopy ####

The Enthought Canopy python distribution exists in two different versions. A basic free version with a 
limited number of packages (Canopy express) and a non free full version. The full version can be obtained 
free of charge for academic use. Register with [Enthought Scientific Computing](https://enthought.com/products/canopy/academic/)
using your UCL e-mail address for an academic licence.

You may then use your Enthought user accout to sign into the installed application and activate the academic version. Canopy comes with a package manager
from where it is possible to install and update a large number of python packaged. The packages installed by default should cover our needs.

If you use this route, you can ignore the distribute \& pip section.

#### Python from python.org ####

Alternative, you can download *Python* from python.org:

If you have a newer Mac, i.e. one from the last few years, 
you should download 
[this version](http://www.python.org/ftp/python/2.7.5/python-2.7.5-macosx10.6.dmg) 
and [follow the instructions](http://www.python.org/download/mac/tcltk/) about Tcl/Tk dependencies.

If you have an older Mac, [follow these instructions](http://www.python.org/getit/releases/2.7.5/ "Python download"),
including OS-version-specific information and important details about Tcl/Tk/TKinter dependencies.

##### distribute \& pip #####

Open terminal (search in spotlight for "terminal" or look in the Applications/Utilities folder) and paste in this:
	
	curl -O http://python-distribute.org/distribute_setup.py
	python distribute_setup.py
	sudo easy_install pip

You will need to enter your administrator password.

### XCode and command line tools ###

Install [XCode](https://itunes.apple.com/us/app/xcode/id497799835) using the Mac app store. 

Then, go to Xcode...Preferences...Downloads... and install the command line tools option

### Git ###

Download and install [Git](https://help.github.com/articles/set-up-git)

Ignore the 'set up git' section.

#### Slightly harder route: via homebrew ####

Install Homebrew via typing this at a terminal:

    ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"
    
and then type

    brew install git

Then install the [GitHub for Mac client](http://mac.github.com).

### Editor and shell ###
The default text editor on OS X *textedit* should be sufficient for our use. Alternatively 
http://mac.appstorm.net/roundups/office-roundups/top-10-mac-text-editors/ lists a number of other good editors. 

To setup git to use *textedit* executing the following in a terminal should do.

```
git config --global core.editor /Applications/TextEdit.app/Contents/MacOS/TextEdit
```

The default terminal on OSX should also be sufficient. If you want a more advanced terminal [iTerm2](http://www.iterm2.com/) is an alternative.

## Windows Users ##

### Python ###
#### Enthought Canopy ####

The Enthought Canopy python distribution exists in two different versions. A basic free version with a 
limited number of packages (Canopy express) and a non free full version. The full version can be obtained 
free of charge for academic use. Register with [Enthought Scientific Computing](https://enthought.com/products/canopy/academic/)
using your UCL e-mail address for an academic licence. After registering download and install the Canopy package for your operating system. 

You may then use your Enthought user account to sign into the installed application. Canopy comes with a package manager
from where it is possible to install and update all the shiped python packaged. The packages installed by default should cover our needs.

To use the IPython notebook on a Windows computer with Sophos antivirus installed it may be necessary to open additional ports
allowing communication between the notebook and its server.
The [solution](http://stackoverflow.com/questions/13036197/ipython-notebook-getting-output) is:

* open your Sophos Endpoint Security and Control Panel from your tray or start menu
* Select "configure" > "Anti-virus" > "Authorization" from the menu at the top
* Select the websites tab
* click the "Add" button and add 127.0.0.1 and localhost to the "Authorized websites" list
* restart computer (most likely not needed, just restart the IPython notebook)
* output works now :)

### Git ###

Install [msysgit](http://code.google.com/p/msysgit/downloads/list?q=full+installer+official+git)

Then install the [GitHub for Windows client](http://windows.github.com/).

### Editor and Shell ###

Msysgit provides git bash which we will use as the default shell on Windows. 

In order to write and edit code examples during the carpentry event a good text editor is essential. 
Unless you already use a specific editor which you are comfortable with we recommend using *Notepad++* on windows.

http://notepad-plus-plus.org/

Using Notepad++ to edit text files including code should be straight forward but in addition you should configure git 
to use notepad++ when writing commit messages (We will learn about these in the version controle session).   

By opening git bash and entering the following we configure git to use the editor located at 
"C:/Program Files/Notepad++/notepad++.exe" to open commit messages. Depending on the version and language of your windows 
installation you might need to adjust this path. You should be able to figure out the corret path by using the windows file explorer to navigate 
to the installation folder of notepad++. 

```
git config --global core.editor "'C:/Program Files/Notepad++/notepad++.exe' -multiInst -nosession -noPlugin"
```

On 64 bit windows7/8 the correct command should be: 

```
git config --global core.editor "'C:/Program Files (x86)/Notepad++/notepad++.exe' -multiInst  -nosession -noPlugin"
```

Note that it is not obvious how to copy and paste text in a Windows terminal including Git Bash. Copy and paste can be found by right
clicking on the top bar and selecting the commands from the drop down menu (in a sub menu).  

Confirm that the installation has worked by opening to 'Git Bash' in the Start Menu and then typing:
	
	python -V
	git --version

This should print the installed version of the python and git confirming that both are installed at working correctly. 