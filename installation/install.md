---
title: RITS Training Installation Instructions
---

Installation Instructions
=========================

Introduction
------------

This document contains instructions for installation of the packages we'll be using during the UCL
Software Carpentry Workshops and our other training courses. You will be following the training on
your own machines, so please complete these instructions.

What we're installing
---------------------

For the software carpentry session on programming, we'll be using the language *Python* and in
particular version 2.7. We will use the *Enthought Canopy* python distribution which contains a good
collection of the most common *Python* modules as well as *IPython* (an improved *Python*
interpreter) and the IPython notebook (a useful web-based user interface that allows you to create
documents that combine text and *Python* code, executable with the same browser window).  We'll need
*pip*, the package installer for *Python*, as well.

For the workshop session on version control, we'll be using *Git* and the *Github* website.

If you're just attending the software carpentry course, and not other RITS courses, you can ignore
the sections on compilers, cmake, and subversion. However, we encourage you to be ready to follow
our other courses, so you might want to complete these instructions too.

A note on systems
-----------------

Linux users should be able to use their package manager to install all of this software (if you're
using Linux, we assume you won't have any trouble with these requirements).

However note that if you are running an older Linux distribution you may get older versions with
different look and features.  A recent Linux distribution is recommended.

Mac and Windows users should follow the instructions below.

Don't panic
-----------

Give yourself 30 minutes or so to run through this installation process and don't get intimidated!
Please try to install everything well before the bootcamp,
as it is important that we don't waste time during the workshop trying to mend installations.

If you do get stuck, first try searching on the internet
(e.g. [stackoverflow.com](http://stackoverflow.com)) for solutions.  Or, try asking a fellow
bootcamp attendee for help.

Drop-in session
---------------

We will be running a drop-in session for people that would like some help with setting up their
laptop in advance of the training. You will have been advised as to when this will occur.

All students should either attend this or ensure that they have a working git, python, and editor
and shell installation by following the instructions bellow before the workshop.

Eduroam
-------

We will be using UCL's [eduroam](http://www.ucl.ac.uk/isd/staff/wireless/eduroam) service to connect
to the internet for this work.

So you should ensure you have eduroam installed and working.

Linux
=====

Python via package manager
--------------------------

Recent versions of Ubuntu (14.04 and 13.10) pack mostly up to date versions of all needed
packages. The version of IPython is however slightly out of date. Advanced users may wish to upgrade
this using ```pip``` or a manual install. On Ubuntu you should ensure that the following packages
are installed using apt-get.

*  python-numpy
*  python-scipy
*  python-nose
*  python-matplotlib
*  python-pip
*  ipython
*  ipython-notebook

Older distributions may have outdated versions of specific packages.
Other linux distributions most likely also contain the needed python packages but again
they may also be outdated.

Python via Enthought Canopy
---------------------------

Alternatively you may install a complete independent scientific python distribution. One of these is
Enthought Canopy.

The Enthought Canopy python distribution exists in two different versions. A basic free version with
a limited number of packages (Canopy express) and a non free full version. The full version can be
obtained free of charge for academic use. Register with
[Enthought Scientific Computing](https://enthought.com/products/canopy/academic/) using your UCL
e-mail address for an academic licence.

You may then use your Enthought user account to sign into the installed Canopy application and
activate the full academic version. Canopy comes with a package manager from where it is possible to
install and update a large number of python packages. The packages installed by default should cover
our needs.

Git
---

If git is not already available on your machine you can try to install it via your distribution
package manager (e.g. `apt-get` or `yum`), for example:

``` bash
sudo apt-get install git
```

Editor
------

Many different text editors suitable for programming are available.  If you don't already have a
favourite, you could look at [Kate](http://kate-editor.org/).

Regardless of which editor you have chosen you should configure git to use it. Executing something
like this in a terminal should work:

``` bash
git config --global core.editor NameofYourEditorHere
```

The default shell is usually bash but if not you can get to bash by opening a terminal and typing `bash`.

Compilers
---------

Those considering following other RITS courses beyond the Software Carpentry should also install a
working C++ compiler. On Linux you are most likely to use g++. On Ubuntu you may either install this
manually or install build-essential which will install everything needed.

``` Bash
sudo apt-get install build-essential
```

Subversion
----------

Again, install the appropriate package with apt-get or yum, for example:

``` Bash
sudo apt-get install subversion
```

CMake
-----

Again, install the appropriate package with apt-get or yum (`cmake`)

Mac
===

Python
------

The Enthought Canopy python distribution exists in two different versions. A basic free version with
a limited number of packages (Canopy express) and a non free full version. The full version can be
obtained free of charge for academic use. Register with
[Enthought Scientific Computing](https://enthought.com/products/canopy/academic/) using your UCL
e-mail address for an academic licence.

You may then use your Enthought user account to sign into the installed application and activate the
academic version. Canopy comes with a package manager from where it is possible to install and
update a large number of python packaged. The packages installed by default should cover our needs.

If you use this route, you can ignore the distribute \& pip section.

Python from Homebrew
--------------------

OSX ships with a resent python version and some packages. However this has known limitations and we
do not recommend it. You can install a new version of python from homebrew with the following.
Please follow the instructions below to install the Xcode tools and homebrew before attempting
this.

```bash
brew install python
```

In order to ensure that this version of python is selected over the OSX default version you should
execute the following command:

```bash
echo export PATH='/usr/local/bin:$PATH' >> ~/.bash_profile
```
and reopen the terminal. Verify that this is correctly installed by executing

```
python --version
```

Which should print:

```
Python 2.7.6
```

brew install [package-name]
*  pkg-config
*  freetype
*  gfortran

pip install [package-name]
*  numpy
*  nose
*  scipy
*  matplotlib
*  ipython[all]

XCode and Command line tools
----------------------------

We do not recommend following this training on older versions of OSX without an app store: upgrade
to OSX Mavericks. It should be possible to complete the instrcutions on any OSX version with the
App store (Snow Leopard (10.6) and newer) However, we reccoment upgrading to Mavericks if possible
since this is the most well tested.

Mavericks:

Install the XCode command-line-tools by opening a terminal and run the following.

```bash
xcode-select --install
```

You may also install Xcode from the Mac app store if you wish, but it is not needed.

Pre Mavericks:

Install [XCode](https://itunes.apple.com/us/app/xcode/id497799835) using the Mac app store.

Then, go to Xcode...Preferences...Downloads... and install the command line tools option.

Homebrew
--------
[Homebrew](brew.sh) is a package manager for OSX which comes with enables the installation of a lot of
software useful for scientific computing. It is required for some of the installations below.
But not essential for Software Carpentry. Homebrew requires the Xcode tools.

Install Homebrew via typing this at a terminal:

``` bash
ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
```

and then type.

```bash
brew doctor
```

And read the output to verify that everything is working as expected.

Git
---

The Xcode command-line-tools comes with git installed at least on OSX 10.8 and later. Verify this by executing:

``` bash
git --version
```
This should print something reasonable such as

``` bash
git version 1.8.5.2 (Apple Git-48)
```

Alternatively you can install git in one of the following ways.

### Homebrew

``` bash
brew install git
```

### Git Without Homebrew

Alternatively, you can install Git directly without Homebrew
via [Git](https://help.github.com/articles/set-up-git). Ignore the 'set up git' section.
Homebrew is the better route, as it will then be easier to obtain other tools you may need later.

CMake
-----

Just do

``` Bash
brew install cmake
```

(If you're not using homebrew, you can get the [package directly](http://www.cmake.org/cmake/resources/software.html))

Editor and shell
----------------

The default text editor on OS X *textedit* should be sufficient for our use. Alternatively
http://mac.appstorm.net/roundups/office-roundups/top-10-mac-text-editors/ lists a number of other good editors.

A new open source option is Github's Atom editor. You can get it from https://atom.io/
However note that this is still in somewhat early development.

To setup git to use *textedit* executing the following in a terminal should do.

``` bash
git config --global core.editor /Applications/TextEdit.app/Contents/MacOS/TextEdit
```

The default terminal on OSX should also be sufficient. If you want a more advanced terminal
[iTerm2](http://www.iterm2.com/) is an alternative.

Windows
=======

Python
------

The Enthought Canopy python distribution exists in two different versions. A basic free version with
a limited number of packages (Canopy express) and a non free full version. The full version can be
obtained free of charge for academic use. Register with
[Enthought Scientific Computing](https://enthought.com/products/canopy/academic/) using your UCL
e-mail address for an academic licence. After registering download and install the Canopy package
for your operating system. If prompted make sure that you select Enthought as your default Python
interpreter.

You may then use your Enthought user account to sign into the installed application. Canopy comes
with a package manager from where it is possible to install and update all the shipped python
packaged. The packages installed by default should cover our needs.

Sophos
------

To use the IPython notebook on a Windows computer with Sophos anti-virus installed it may be necessary to
open additional ports allowing communication between the notebook and its server.
The [solution](http://stackoverflow.com/questions/13036197/ipython-notebook-getting-output) is:

* open your Sophos Endpoint Security and Control Panel from your tray or start menu
* Select "configure" > "Anti-virus" > "Authorization" from the menu at the top
* Select the websites tab
* click the "Add" button and add 127.0.0.1 and localhost to the "Authorized websites" list
* restart computer (most likely not needed, just restart the IPython notebook)
* output works now :)

Git
---

Install [msysgit](http://msysgit.github.io/)

Then install the [GitHub for Windows client](http://windows.github.com/). This comes with both a GUI
client as well as the [msysgit](http://msysgit.github.io/) terminal client which we will use in
Software Carpentry. You should register with [Github](github.com) for an account and sign into the
GUI client with this account. This will automatically set-up
[SSH based authentication](https://help.github.com/articles/generating-ssh-keys#platform-windows)
for the terminal client. The terminal client comes in 3 different flavours based on Windows CMD (dos
like), Windows Powershell, and BASH. We will use the BASH client as this most closely resembles the
Linux and OS X terminal used by other students. In order to configure this open the Github
client. Sign in with your credentials and:

*  Select tools
*  Options
*  Default Shell
*  Git Bash
*  And Press Update to save.

Verify that this is working by opening the Git shell. The Shell window should have a title that
starts with MINGW32.

Editor
------

Unless you already use a specific editor which you are comfortable with we recommend using
[Notepad++](http://notepad-plus-plus.org/). Follow the [download link.](http://notepad-plus-pl
us.org/)

Using Notepad++ to edit text files including code should be straight forward but in addition you
should configure git to use notepad++ when writing commit messages (We will learn about these in the
version control session). The following sections goes through this:

Finding out where things got installed
--------------------------------------

Now, we need to find out where Notepad++ have been installed, this will be either in `C:/Program
Files (x86)` or in `C:\ProgramFiles`. The former is the norm on more modern versions of windows. If
you have the older version, replace `Program\ Files\ \(x86\)` with `Program\ Files` in the
instructions below. If you are unsure about this open Windows explore and navigate to the C
drive. If the C drive contains both a `Program Files (x86)` and `Program Files` folder Notepad++ is
most likely to be installed in `Program Files (x86)`. Verify this by opening the folder and look for
a `Notepad++` subfolder. On a non English widows installation the directories may have different names.
You should however still use the English names. Just verify if the directory ends with (x86) or
not.

Telling the shell where to find Notepad++
-----------------------------------------

We need to tell the new shell installed with Git where Notepad++ is.

In order to do this we will edit a Widows environmental Variable called ```PATH```
This is basically a list of directories separated by ':' where the shell will look for
programs.

To do this:

*  Open the control panel
*  Select system
*  Advanced system settings
*  Environment Variables
*  Select Path and press edit.

This will open a Dialog box with a long string ```Variable value:```
At the end of the string you should add ```;C:\Program Files (x86)\Notepad++```
Where you substitute ```Program Files (x86)``` with the directory determined above.


Testing your install
--------------------

Check this works by opening the Github shell. Once you have a terminal open, type

``` bash
which notepad++
```

which should produce readout similar to `/c/Program Files (x86)/Notepad++/notepad++.exe`

Also verify the typing:
```bash
notepad++
```
opens the editor and the close it again.

``` bash
which git
```

which should produce `/c/Program Files (x86)/Notepad++/notepad++.exe` or `/bin/git`. The ``which``
command is used to figure out where a given program is located on disk.

Telling Git about Notepad
-------------------------

Now we need to update the default editor used by Git.

``` bash
git config --global core.editor "'notepad++.exe' -multiInst  -nosession -noPlugin"
```

Note that it is not obvious how to copy and paste text in a Windows terminal including Git Bash.
Copy and paste can be found by right clicking on the top bar of the window and selecting the
commands from the drop down menu (in a sub menu).

Testing python
--------------

Confirm that the Python installation has worked by typing:

``` bash
python -V
```

Which should result in details of your installed python version.

This should print the installed version of the python and git confirming that both are installed at
working correctly.

You should now have a working version of git, python, and notepad++, all accessible from your shell.

Subversion
----------

You only need subversion if you are following RSDT courses beyond Software Carpentry.
Install [subversion](http://sourceforge.net/projects/win32svn/)

And choose to add it to the path for all users if so prompted.

CMake
-----

You only need CMake if you are following RSDT courses beyond Software Carpentry.
Install [cmake](http://www.cmake.org/cmake/resources/software.html)

And choose to add it to the path for all users if so prompted.

Testing cmake and subversion
----------------------------

Check that cmake and subversion work from your Git shell:

``` Bash
which cmake
which svn
```


