# UCL ![Software Carpentry logo](http://software-carpentry.org/img/software-carpentry-banner.png "Software Carpentry logo") Bootcamp 4th and 8th April 2013: Installation Instructions #

This document contains instructions for installation of the packages
we'll be using during the Software Carpentry Workshop on the 4th and 8th April 2013.

For the session on programming,
we'll be using the language *Python* and in particular version 2.7.
We'll need *pip*, the package installer for *Python*, as well.

For our database work, we'll need *SQLite 3*,
and the *Firefox* web-browser with the *SQLite add-on*.

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

The default shell is usually bash but if not you can get to bash by opening a terminal and typing `bash`.

If git is not already available on your machine 
you can try to install it via your distribution package manager (e.g. `apt-get` or `yum`).

Many different text editors suitable for programming are available.
If you don't already have a favourite,
you could look at [Kate](http://kate-editor.org/).

## Mac Users ##

### Python 2.7 ###

The easiest option is to register with [Enthought Scientific Computing](https://www2.enthought.com/licenses/academic)
using your UCL e-mail address.

Then follow the instructions in the e-mail they send you.
Navigate to `repository-login/installers`, then download and install the OSX install package.
If you use this route, you can ignore the distribute \& pip section.

Alternative, you can download *Python* from python.org:

If you have a newer Mac, i.e. one from the last few years, 
you should download 
[this version](http://www.python.org/ftp/python/2.7.3/python-2.7.3-macosx10.6.dmg) 
and [follow the instructions](http://www.python.org/download/mac/tcltk/) about Tcl/Tk dependencies.

If you have an older Mac, [follow these instructions](http://www.python.org/getit/releases/2.7.3/ "Python download"),
including OS-version-specific information and important details about Tcl/Tk/TKinter dependencies.

### distribute \& pip ###

Open terminal (search in spotlight for "terminal" or look in the Applications/Utilities folder) and paste in this:
	
	curl -O http://python-distribute.org/distribute_setup.py
	python distribute_setup.py
	sudo easy_install pip

You will need to enter your administrator password.

### SQLite3###

#### Slightly easier route: installing a pre-compiled package ####


Download the [pre-compiled binary](http://www.sqlite.org/sqlite-shell-osx-x86-3071502.zip)

#### Slightly harder route: compiling from source ####


Download a compressed "Tarball" of [SQLite 3](http://www.sqlite.org/sqlite-autoconf-3071502.tar.gz) and then open a terminal window.

First, navigate to the directory to which you downloaded the tarball (you can drag a folder from finder into the terminal window.

So type `cd <space>` then drag in the folder from finder (you'll see the file path appear in the terminal window).

Then run the following commands, pressing `enter` after each line:

	./configure
	make
	[sudo] make install

After this has finished, test it's working by typing `sqlite3` at the prompt

### Firefox ###

Pretty straightforward - download and install from the [firefox website](http://firefox.com/)

### Firefox SQLite 3 add-on ###

Go into Firefox/Add-ons and search for *SQLite*. Install the *SQLite Manager*.

### Git ###

First, download and install [Git](https://help.github.com/articles/set-up-git)

Ignore the 'set up git' section.

Then install the [GitHub for Mac client](http://mac.github.com).

## Windows Users ##

Windows users will install a pre-packages version of Python that includes all the required packages.
Python will be accessed using the msysgit shell (command prompt) installed in the 

### Python 2.7 ###

Install [Anaconda CE Python](http://continuum.io/anacondace.html) distribution.

This includes *pip*, *distribute*, *nose* and *pytest*, so your work here is done.

### Git ###

Next, install [msysgit](http://code.google.com/p/msysgit/downloads/list?q=full+installer+official+git)

Then install the [GitHub for Windows client](http://windows.github.com/).

### Editor and Shell ###

Run [swc_windows_installer.py](https://raw.github.com/swcarpentry/boot-camps/master/setup/swc-windows-installer.py).
Download the file and save as *swc_windows_installer.py*.
You should be able to simply double click the file in Windows.

Confirm that this has worked by opening to 'Git Bash' in the Start Menu and then typing:
	
	python -V
	git --version
	nano -V
    
The version numbers of *Python*, *Git* and *nano* (a text editor) should be displayed.

### SQLite3 ###

This software is available [here](http://www.sqlite.org/download.html).

Windows users should select the *Precompiled Binaries for Windows, command-line shell*.

### Firefox ###
Download from the [Firefox website](http://firefox.com/) and install.

### Firefox SQLite 3 add-on ###

Go into Firefox | Add-ons and search for *Sqlite*. Install the *SQLite Manager*.



