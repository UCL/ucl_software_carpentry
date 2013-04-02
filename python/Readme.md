# UCL Software Carpentry boot camp: 
# Introduction to Python

* * * *

**Based on the material available at https://github.com/swcarpentry/**

**Distributed under CC BY-SA 2.0 UK licence**

## Introduction
This lecture is on basic programming in python. In order to do the examples, we are going to use an environment called iPython notebook.  I expect this lecture to be interactive, so stop me at any point if you have questions. The correct power dynamic is that people are the masters and the machines are servants. The computer is a hammer; it exists to help us get things done.  We can hammer nails with the handle, with the claw of the hammer; some of us even hammer nails with bricks.  But when you learn what part of the hammer works best with nails, and have some experience swinging it, you spend less time worrying about the hammering and more time worrying about your furniture.

This lecture will be structured as follows: I will be teaching the basics of two things: the python programming language (to a greater extent) and the ipython interpreter (to a lesser extent). The ipython interpreter is one of many different ways to implement python code. As far as the python component, I'll shoot for a layered approach: I'l continue building on my previous concepts. It turns out that like any sufficiently complex topic, its not really possible to force the pedagogy into a serial stream. Also, we have a pretty serious time constraint. I'm just going to drop it on you. Because of the brief nature of this tutorial, I've included links to some excellent reference material. Also, if we have time, I'll take questions based on the specific programming needs of this class.

Here is the reference material.

* [Dive into Python] (http://www.diveintopython.net/toc/index.html)
* [Software Carpentry's Python Lectures] (http://software-carpentry.org/4_0/python/)
* [IPython: A System for Interactive Scientific Computing] (http://dx.doi.org/10.1109/MCSE.2007.53)
* [How to Think Like a Computer Scientist] (http://www.greenteapress.com/thinkpython/thinkpython.html)

Once we briefly deal with ipython, I'll cover python in the following order:

## What I'll cover
### Lesson 1
* print statements
* variables
* integers
* floats
* strings
* types
* type coersion
* basic operations: add numbers, concatenate strings, basic data type functionality

### Lesson 2
* list
* dictionary 
* set 
* tuple
* file reading

### Lesson 3
* for loop
* conditional (if) statements
* while loops
* iteration
* writing to files

### Lesson 4
* methods
* modules

## What you should explore on your own

### Lesson 5
* Strings
* File I/O

### Lesson 6
* Object orientation in Python
* Classes vs objects
* Inheritance

### Lesson 7
* Matplotlib

### Lesson 8
* Scipy

### Lesson 9
* Numpy

## iPython
You can run python commands in a handful of ways; you can create executable scripts, you can run the python interpreter, you can run iPython, or you can run iPython notebook.  iPython is an alternative to the built-in Python interpreter with some nice features.  iPython notebook gives you interactive access to the python interpreter from within a browser window, and it allows you to save your commands as a "notebook".
Lets give the built-in interpreter a spin just this once.

```
swc@swc:~$ python
Python 2.7.3 (default, Apr 20 2012, 22:44:07) 
[GCC 4.6.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> print "hello world"
hello world
>>> quit() 
```

We can also write python commands in a file and execute them from the command line. You will notice that the print command above is located in the file hello.py. Execute the following command at the command line

```
swc@swc:~$ python hello.py
```

iPython has more useful features for interactive use than the standard python interpreter, so we'll use it from here on out.

```python
swc@swc:~$ ipython notebook
In [1]: print "hello world"
hello world
In [2]: 
```

You may notice if you hit ENTER your current command does not execute.  ENTER puts a line break in your current command, and allows you to write multi-line commands and have them all executed at once.  
SHIFT-ENTER sends the line that your cursor is on to the interpreter.  The output of the command, or the error message, appears below the line you entered it on.

```
In [2]: print "hello"
        print "world"
hello
world
In [3]: 
```

### Pasting

You can paste things into the ipython console by copying text from your machine with **ctrl+c** (or cmd+c) and typing **%paste** at the iPython prompt.

### History

iPython has a history. If you press the up and down keys, you can access the history.

### Tab Completion

iPython also has tab completion of previous commands. Try typing "print" and then hit the tab key.

### Getting Help

iPython has some nice help features. Lets say we want to know more about the integer data type. There are at least two ways to do this task:

```python
In [1] help(int)
```

or 

```python
In [1] int?
```

If you wanted to see all the commands available for something, use the dir command. Check out all of the methods of the str type.

```python
In [1] dir(str)
```

### Executing code in files

If your code is in a file, you can execute it from the iPython shell with the **%run** command. Execute hello.py like so

```python
In [1] %run hello.py
```

### Clearing iPython

To clear everything from iPython, use the reset command.

```python
In [1] reset
Once deleted, variables cannot be recovered. Proceed (y/[n])?
```



