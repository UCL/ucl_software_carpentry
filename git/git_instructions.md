UCL Git and GitHub training
===========================

In this module, you will learn how to manage your code with Version Control. This will allow you to see the history of your code, roll back mistakes, to collaborate smoothly with other people on the same code, and to publish your code to the internet for other people to use.

This course will use the `git` version control system, but much of what you learn will be valid with other version control tools you may encounter, including subversion (`svn`) and mercurial (`hg`).

This version of the content assumes you will interact with Git through the Git command line. There is an alternative version of the content which uses the GitHub Windows and Mac clients [here](git_gui_instructions.md).

In this course, we will use, as an example, the development of a few text files containing a description of a topic of your choice. This could be your research, a hobby of yours, or something else. In the end, we will show you how to display the content of these files as a very simple website. The text files we create will use a simple "wiki" markup style called [markdown](http://daringfireball.net/projects/markdown/basics) to show formatting. This is the convention used in this file, too. You can view the content of this file in the way Markdown renders it by looking on the [web](https://github.com/UCL/ucl_software_carpentry/blob/master/git/git_instructions.md), and see compare the [raw text](https://raw.github.com/UCL/ucl_software_carpentry/master/git/git_instructions.md).

The purpose of this exercise is to learn how to use Git to manage program code you write, not simple text website content, but we'll just use these text files instead of code for now, so as not to confuse matters with trying to learn version control while thinking about programming too. On the second day of the bootcamp, you should use the version control tools you learn today as you work on that day's exercises. 

Section 1: Solo work
--------------------

This tutorial is based on use of the Git command line. Commands you can type will look like this:

    echo some output
    
and results you should see will look like this:

> some output

First, we should configure Git to know our name and email address:

    git config --global user.name "Your Name Here"
    git config --global user.email "your_email@ucl.ac.uk"

Create a folder to do your work in:

    mkdir my_swcarpentry_solutions/
    mkdir my_swcarpentry_solutions/my_swcarpentry_git_solution
    cd my_swcarpentry_solutions/my_swcarpentry_git_solution

Now, we will tell Git to track the content of this folder as a git "repository".

    git init

> Initialized empty Git repository in ...my_swcarpentry_solutions/my_swcarpentry_git_solution

As yet, this repository contains no files:

    ls output
    git status

>    # On branch   
>    #  
>    # Initial commit  
>    #  
>    nothing to commit (create/copy files and use "git add" to track) 

So let's create an example file, and see how to start to manage a history of changes to it. I'm going to be using `vim` as my editor, but you can use whatever editor you prefer. (Windows users should use "Notepad++", Mac users could use "textmate" or "sublime text", linux users could use `vim`, `nano` or `emacs`.) I'm calling this file `index.md`, because it'll be important when we try to publish our website later.

    vim index.md # Type some content into the file.
    cat index.md

>    Mountains in the UK   
>    ===================   
>    England is not very mountainous.   
>    But has some tall hills, and maybe a mountain or two depending on your definition.    

So, let's tell Git that `index.md` is a file which is important, and we would like to keep track of its history:

    git add index.md
   
* Don't forget: Any files in repositories which you want to "track" need to be added with `git add` after you create them.

Now, we need to tell Git to record the first version of this file in the history of changes:

    git commit
    
With any luck, an editor has just popped up, into which you can provide a "commit message": a note as to what this revision changes in the file. If you don't like your editor, you can change it with:

    git config --global core.editor nano
    
I'm happy with vim, so I'll just set my commit message, save, and quit:

> First commit of discourse on UK topography

And note the confirmation from Git:

> [master (root-commit) c438f17] First commit of discourse on UK topography  
> 1 file changed, 6 insertions(+)  
> create mode 100644 index.md   

There's a lot of output there you can ignore for now, it'll (mostly) make sense later!

The important thing is that now, we can see that git has one change in its history:

    git log
   
>   commit c438f1716b2515563e03e82231acbae7dd4f4656     
>   Author: James Hetherington <j.hetherington@ucl.ac.uk>    
>   Date:   Wed Apr 3 15:32:33 2013 +0100   

>       First commit of discourse on UK topography     

As well as the commit message, author, and date, the commit "hash code", `c438f1716b2515563e03e82231acbae7dd4f4656` is a unique identifier of that particular revision. (This is a really long code, but whenever you need to use it, you can just use the first few characters, however many characters is long enough to make it unique.)

Note that git will now tell us that our "working directory" is up-to-date with the repository: there are no changes to the files that aren't recorded in the repository history:

    git status
    
>     # On branch master
>    nothing to commit (working directory clean)

But I'm going to make a change to the file:

    vim index.md
    cat index.md
    
>    Mountains in the UK  
>    ===================   
>    England is not very mountainous.  
>    But it has some tall hills, and maybe a mountain or two depending on your definition.  
>    Mount Fictional, in Barsetshire, U.K. is the tallest mountain in the world.   


    git status

>    # On branch master  
>    # Changes not staged for commit:  
>    #   (use "git add <file>..." to update what will be committed)  
>    #   (use "git checkout -- <file>..." to discard changes in working directory)  
>    #  
>    #	modified:   index.md  
>    #  
>    no changes added to commit (use "git add" and/or "git commit -a")   

We can now see that there is a change to "index.md" which is currently "not staged for commit". What does this mean? It means that if we do a `git commit` now *nothing will happen*. This is because, git will only commit changes to files that you choose to include in each commit. This is a difference from other version control systems, where committing will commit changes to all tracked files. To include the file in the next commit, we have a few choices. This is one of the things to be careful of with git: there are lots of ways to do similar things, and it can be hard to keep track of them all. We're going to do:

    git add --update

This says "include in the next commit, all files which have ever been included before". Note that `git add` is the command we use to introduce git to a new file, but also the command we use to "stage" a file to be included in the next commit. The "staging area" is the git jargon for the place which contains changes which will be included in the next commit.

    git status
    
>    # On branch master  
>    # Changes to be committed:  
>    #   (use "git reset HEAD <file>..." to unstage)  
>    #  
>    #	modified:   index.md  
>    #  

    git commit
    git log
    
>    commit 50280520d33592d093773dfd3e5de4c3da7e1a09  
>    Author: James Hetherington <j.hetherington@ucl.ac.uk>  
>    Date:   Wed Apr 3 15:49:02 2013 +0100  
>
>        Add a lie about a mountain  
>
>    commit c438f1716b2515563e03e82231acbae7dd4f4656  
>    Author: James Hetherington <j.hetherington@ucl.ac.uk>  
>    Date:   Wed Apr 3 15:32:33 2013 +0100  
>
>        First commit of discourse on UK topography  

Great, we now have a file which contains a mistake.

In a while, we'll use Git to roll back to the last correct version: this is one of the main reasons we wanted to use version control, after all! But for now, let's do just as we would if we were writing code, not notice our mistake and keep working...

    vim index.md
    cat index.md
    
>  Mountains and Hills in the UK  

    git commit -a
    
This last command, `git commit -a` automatically adds changes to all tracked files to the staging area, as part of the commit command. So, if you never want to just add changes to some tracked files but not others, you can just use this and forget about the staging area!

    git log | head
    
> commit 0bae9055dca14f659154e1d9a50409751b59aad8 
> Author: James Hetherington <j.hetherington@ucl.ac.uk>  
> Date:   Wed Apr 3 15:55:38 2013 +0100  
>  
>    Change title  

We now have three changes in the history:
 
    git log --oneline

> 0bae905 Change title  
> 5028052 Add a lie about a mountain  
> c438f17 First commit of discourse on UK topography  
 
2. Fixing Mistakes
------------------
 
Ok, so now we'd like to undo the nasty commit with the lie about Mount Fictional.

    git revert --in 5028

A commit window pops up, with some default text which you can accept and save. 

You may, depending on the changes you've tried to make, get an error message here. If this happens, it is because git could not automagically decide how to combine the change you made after the change you want to revert, with the attempt to revert the change: this could happen, for example, if they both touch the same line. If that happens, you need to manually edit the file to fix the problem, ask your demonstrator for help.
    
The file should now contain the change to the title, but not the extra line with the lie. Note the log:

> commit d6959031d5722cb2b22c408e704e894bce7713e9  
> Author: James Hetherington <j.hetherington@ucl.ac.uk>  
> Date:   Wed Apr 3 16:13:19 2013 +0100  
>    Revert "Add a lie about a mountain"  
>    This reverts commit 50280520d33592d093773dfd3e5de4c3da7e1a09.   

Notice how the mistake has stayed in the history: you can see a commit which undoes the change: this is colloquially called an "antipatch". This is nice: you have a record of the full story, including the mistake and its correction.

It is possible, in git, to remove the most recent change altogether, "rewriting history". Let's make another bad change, and see how to do this.

    vim index.md
    cat index.md

> Engerland is not very mountainous.  

    git commit -a
    git log | head

> ...Add a silly spelling    
    
    git reset HEAD^

> Unstaged changes after reset:  
> M	index.md      
 
    git log --oneline

>    53f4b50    Revert "Add a lie about a mountain"     This reverts commit 50280520d  
>    0bae905 Change title  
>    5028052 Add a lie about a mountain  
>    c438f17 First commit of discourse on UK topography  

The silly spelling is gone, and *it isn't even in the log*. This approach to fixing mistakes, "rewriting history" with `reset`, instead of adding an antipatch with `revert` is dangerous, and we don't recommend it. But you may want to do it for small silly mistakes, such as to correct a commit message.

When git reset removes commits, it leaves your working directory unchanged -- so you can keep the work in the bad change if you want. If you want to lose the change from the working directory as well, you can do `git reset --hard`. I'm going to get rid of the silly spelling, and I didn't do `--hard`, so I'll reset the file from the working directory to be the same as in the repository (after removing the reset):

    git checkout index.md
    

Section 2: Publishing
---------------------


Section 3: Collaboration
------------------------
