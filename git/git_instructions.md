UCL Git and GitHub training
===========================

In this module, you will learn how to manage your code with Version Control. This will allow you to see the history of your code, roll back mistakes, to collaborate smoothly with other people on the same code, and to publish your code to the internet for other people to use.

This course will use the `git` version control system, but much of what you learn will be valid with other version control tools you may encounter, including subversion (`svn`) and mercurial (`hg`).

This version of the content assumes you will interact with Git through the Git command line. There is an alternative version of the content which uses the GitHub Windows and Mac clients [here](git_gui_instructions.md).

In this course, we will use, as an example, the development of a few text files containing a description of a topic of your choice. This could be your research, a hobby of yours, or something else. In the end, we will show you how to display the content of these files as a very simple website. The text files we create will use a simple "wiki" markup style called markdown to show formatting. This is the convention used in this file, too. You can view the content of this file in the way Markdown renders it by looking at , and see the raw text at . 

The purpose of this exercise is to learn how to use Git to manage your code, but we'll just use these text files instead of code for now, so as not to confuse matters with trying to learn version control while thinking about programming too. On the second day of the bootcamp, you should use the version control tools you learn today as you work on that day's exercises. 

Section 1: Solo work
--------------------

Create a folder to do your work in:

    mkdir my_swcarpentry_solutions/my_swcarpentry_git_solution
    cd my_swcarpentry_git_solution

Now, we will tell Git to track the content of this folder as a git "repository".

    git init

> Initialized empty Git repository in ...my_swcarpentry_solutions/my_swcarpentry_git_solution

As yet, this repository contains no files:

    ls output
    git status

>    # On branch master

>    #

>    # Initial commit

>    #

>    nothing to commit (create/copy files and use "git add" to track)

Section 2: Publishing
---------------------

Section 3: Collaboration
------------------------
