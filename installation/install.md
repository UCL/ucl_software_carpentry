# UCL ![Software Carpentry logo](http://software-carpentry.org/img/software-carpentry-banner.png "Software Carpentry logo") Bootcamp Thursday 26th and Friday 27th September, 2013: Installation Instructions #

This document contains instructions for installation of the packages
we'll be using during the Software Carpentry Workshop on the 26th and 27th September, 2013
For the session on programming,
we'll be using the language *Python* and in particular version 2.7. We will use the *Enthought Canopy* 
python distribution which contains a good collection of the most common *Python* modules as well as *IPython* 
(an improved *Python* interpreter) and the IPython notebook (a useful web-based user interface that allows
you to create documents that combine text and *Python* code, executable with the same browser window).
We'll need *pip*, the package installer for *Python*, as well.

For the workshop session on version control, 
we'll be using *Git* and the *Github* website.

Linux users should be able to use their package manager to install all of this software
(if you're using Linux, we assume you won't have any trouble with these requirements).
Mac and Windows users should follow the instructions below.

Give yourself 30 minutes or so to run through this installation process and don't get intimidated!
Please try to install everything well before the bootcamp,
as it is important that we don't waste time during the workshop trying to mend installations.

If you do get stuck, first try searching on the internet (e.g. [stackoverflow.com](http://stackoverflow.com)) for solutions.
Or, try asking a fellow bootcamp attendee for help.
Finally, your department should organise a session before the bootcamp to help with any issues.

## Linux Users ##

### Enthought Canopy ###

Register with [Enthought Scientific Computing](https://www2.enthought.com/licenses/academic)
using your UCL e-mail address.

Then follow the instructions in the e-mail they send you. Once your license is active, you will be able
to access the online repository. Navigate to `/repo/epd/installers`, then download and install the 
relevant Linux install package.

### Git ###

If git is not already available on your machine 
you can try to install it via your distribution package manager (e.g. `apt-get` or `yum`).

### Editor and shell ###

Many different text editors suitable for programming are available.
If you don't already have a favourite,
you could look at [Kate](http://kate-editor.org/).

The default shell is usually bash but if not you can get to bash by opening a terminal and typing `bash`.

## Mac Users ##

### Enthought Canopy ###

Register with [Enthought Scientific Computing](https://www2.enthought.com/licenses/academic)
using your UCL e-mail address.

Then follow the instructions in the e-mail they send you.
Then follow the instructions in the e-mail they send you. Once your license is active, you will be able
to access the online repository. Navigate to `/repo/epd/installers`, then download and install the 
relevant OSX package.
If you use this route, you can ignore the distribute \& pip section.

Alternative, you can download *Python* from python.org:

If you have a newer Mac, i.e. one from the last few years, 
you should download 
[this version](http://www.python.org/ftp/python/2.7.5/python-2.7.5-macosx10.6.dmg) 
and [follow the instructions](http://www.python.org/download/mac/tcltk/) about Tcl/Tk dependencies.

If you have an older Mac, [follow these instructions](http://www.python.org/getit/releases/2.7.5/ "Python download"),
including OS-version-specific information and important details about Tcl/Tk/TKinter dependencies.

### distribute \& pip ###

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

## Windows Users ##

### Anaconda Python ###

Install [Anaconda CE Python](http://continuum.io/anacondace.html) distribution.

This includes *pip*, *distribute*, *nose* and *pytest*, so your work here is done.

Python will be accessed using the IPython notebook and the msysgit shell (command prompt) installed in the steps below.

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

Download the python install script [swc_windows_installer.py](https://raw.github.com/swcarpentry/boot-camps/master/setup/swc-windows-installer.py) 
and save the file as  *swc_windows_installer.py*
(you may need to right-click and choose `Save link as`, depending on your browser).
You should be able to simply double click the file in Windows to run it.

If the double-click does not work, then:

Add the python path to windows by following [these instructions](http://stackoverflow.com/questions/6318156/adding-python-path-on-windows-7?answertab=votes#tab-top).
You will need to add `;C:\Anaconda` to the path variable (the directory of your Anaconda Python install).

Then, opening a command prompt (press the `Windows` key, then type `command` in the search prompt),
navigate to your download directory by using, for example,  `cd downloads`.  Then type `python swc-windows-installer.py`.

Confirm that this has worked by opening to 'Git Bash' in the Start Menu and then typing:
	
	python -V
	git --version
	nano -V
    
The version numbers of *Python*, *Git* and *nano* (a text editor) should be displayed.
If *nano* does not install correctly, no problem - just use *Notepad++*...

### Notepad++ ###

Install the Notepad++ editor.

http://notepad-plus-plus.org/download/v6.3.1.html
