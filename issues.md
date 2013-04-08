# Some issues identified during the days

## Internet
* Eduroam not set up on some laptops
* Eduroam connectivity flaky - this is due to the lack of DHCP leases available. Solutions - use alternative temporary internet solution, turn off other devices (e.g. phones) that use wifi.

## Coordination
* Not clear where people to go to at beginning - signs for tables?
* Tension between grouping individuals by departmental teams versus by platform
* Name badges / identifiers for demonstrators
* Not easy to see who had finished exercise/was ready for next step - use green post-its

## Software versions, conflicts and installation problems
* iPython notebook on Windows
* Different versions of iPython notebook on Mac and Windows - Windows using Anaconda, while Mac users are using Enthought
* Bombarding Windows users with use of a text editor such as vim is a bit nasty.  We could include link to Wordpad or TextPad in the setup script.

## Facilities 
* Many power sockets in G20 were not working (fuse blown?)
* power sockets in G20 are not physically suitable for block mac power adapters (need a power plug on cord)
* Coffee vending machine broken on the 8th!
* Hard to walk between rows when students seated back-to-back

## Tricky problems found in exercises
* One person had `nosetests` not finding her tests, due to them having the executable flag set.  See http://stackoverflow.com/questions/1457104/nose-unable-to-find-tests-in-ubuntu.  Fix by changing the flag or using `nosetests --exe`.  `nosetests -vv` is useful for debugging this.

## Other
* Unable to view text in SQLite Manager - see http://code.google.com/p/sqlite-manager/issues/detail?id=520 (In SQLite options, set open in new tab not new window, then use Firefox's normal zoom.)
* GitHub requires horizontal scrolling when you increase font size :(
