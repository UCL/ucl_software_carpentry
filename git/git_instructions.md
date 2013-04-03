UCL Git and GitHub training
===========================

In this module, you will learn how to manage your code with Version Control. This will allow you to see the history of your code, roll back mistakes, to collaborate smoothly with other people on the same code, and to publish your code to the internet for other people to use.

This course will use the `git` version control system, but much of what you learn will be valid with other version control tools you may encounter, including subversion (`svn`) and mercurial (`hg`).

This version of the content assumes you will interact with Git through the Git command line. There is an alternative version of the content which uses the GitHub Windows and Mac clients [here](git_gui_instructions.md).

In this course, we will use, as an example, the development of a few text files containing a description of a topic of your choice. This could be your research, a hobby of yours, or something else. In the end, we will show you how to display the content of these files as a very simple website. The text files we create will use a simple "wiki" markup style called [markdown](http://daringfireball.net/projects/markdown/basics) to show formatting. This is the convention used in this file, too. You can view the content of this file in the way Markdown renders it by looking on the [web](https://github.com/UCL/ucl_software_carpentry/blob/master/git/git_instructions.md), and see compare the [raw text](https://raw.github.com/UCL/ucl_software_carpentry/master/git/git_instructions.md).

The purpose of this exercise is to learn how to use Git to manage program code you write, not simple text website content, but we'll just use these text files instead of code for now, so as not to confuse matters with trying to learn version control while thinking about programming too. On the second day of the bootcamp, you should use the version control tools you learn today as you work on that day's exercises. 

1. Solo work
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

Here, HEAD^ refers to the commit before the "head", which is the latest change. That is, we want to go back to the change before the current one. We could have used the hash code to reference this, but you can also refer to the commit before the HEAD as HEAD^, the one before that as HEAD^^, the one before that as HEAD~3 etc.

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
    

3. Publishing
---------------------

So far, all our work has been on our own computer. But a big part of the point of version control is keeping your work safe, on remote servers. In this example, we'll be using the "GitHub" cloud repository to store our work. 

First, you should create an account on GitHub: go to [GitHub](https://github.com/), fill in a username and password, and click on "sign up for free". 

You'll probably want to set things up so that you don't have to keep typing in your password whenever you interact with GitHub via the command line. One way is via password caching. On the GitHub website there are [instructions](https://help.github.com/articles/set-up-git) to help with this too. Follow them (under "password caching at the link above"). Another way to do this is with an "ssh keypair". The instructions for this are also [on the GitHub website](https://help.github.com/articles/generating-ssh-keys). Ask your demonstrator for help here if you need it.

Ok, let's create a repository to store our work. Hit "new repository" on the right of the github home screen, or click [here](https://github.com/new). Fill in a short name, and a description. Choose a "public" repository. Don't choose to add a Readme.

For this software carpentry course, you should use public repositories in your personal account for your example work: it's good to share! GitHub is free for open source, but in general, charges a fee if you want to keep your work private. In the future, you might want to keep your work on GitHub private: students can get free private repositories on GitHub, by going to [https://github.com/edu] and filling in a form. UCL Research Software Development can support your research group with the cost of private repositories if you need it: get in touch at rc-softdev@ucl.ac.uk for more details.

Instructions will appear, once you've created the repository, as to how to add this new "remote" server to your repository, in the lower box on the screen. Mine say:

    git remote add origin git@github.com:jamespjh/jh-ucl-swcarpentry-answers.git
    git push -u origin master

Follow these instructions.

The first command sets up the server as a new remote, called "origin". Git, unlike some earlier version control systems is a "distributed" version control system, which means you can work with multiple remote servers. Usually, commands that work with remotes allow you to specify the remote to use, but assume the "origin" server if you don't. Here, `git push` will push your whole history onto the server, and now you'll be able to see it on the internet! Refresh your web browser where the instructions were, and you'll see your repository! 

Take a few moments to click around and work your way through the GitHub interface. Try clicking on 'index.md' to see the content of the file: notice how the markdown renders prettily.

Click on "commits" near the top of the screen, to see all the changes you've made. Click on the commit number next to the right of a change, to see what changes it includes: removals are shown in red, and additions in green.

Let's make some more changes, and see how to publish them to GitHub as we go.

4. Multiple files
------------------------

So far, we've only worked with one file. Let's add another:

    vim lakeland.md
    cat lakeland.md
    
>    Lakeland  
>    ========   
>  
>    Cumbria has some pretty hills, and lakes too.  

    git commit -a

>   # On branch master
>    # Untracked files:
>    #   (use "git add <file>..." to include in what will be committed)
>    #
>    #	lakeland.md
>    nothing added to commit but untracked files present (use "git add" to track)

This didn't do anything, because we've not told git to track the new file yet.

    git add lakeland.md
    git commit -a

Ok, now we have added the change to Cumbria to the file. Let's publish it to the origin repository.

    git push
    
>    Counting objects: 4, done.  
>    Delta compression using up to 8 threads.  
>    Compressing objects: 100% (3/3), done.  
>    Writing objects: 100% (3/3), 343 bytes, done.  
>    Total 3 (delta 0), reused 0 (delta 0)  
>    To git@github.com:jamespjh/jh-ucl-swcarpentry-answers.git  
>       53f4b50..9e8b69c  master -> master    

Visit GitHub, and notice this change is on your repository on the server. We could have said `git push origin` to specify the remote to use, but origin is the defaut

Note that you can also make changes in the GitHub website itself. Visit one of your files, and hit "edit".

Make a change in the edit window, and add an appropriate commit message.

That change now appears on the website, but not in your local copy. (Verify this). To get the change into your local copy, do:

    git pull
    
>    remote: Counting objects: 5, done.  
>    remote: Compressing objects: 100% (3/3), done.  
>    remote: Total 3 (delta 1), reused 0 (delta 0)  
>    Unpacking objects: 100% (3/3), done.  
>    From github.com:jamespjh/jh-ucl-swcarpentry-answers  
>       9e8b69c..d2a1854  master     -> answers/master  
>    Updating 9e8b69c..d2a1854  
>    Fast-forward  
>     index.md | 8 ++++++++  
>     1 file changed, 8 insertions(+)   

and check the change is now present on your local version. `git pull` will fetch changes on the server into your local copy: this is important when you are collaborating with others, as we shall see.
 
7. Branching and tagging
------------------------

Git lets you maintain different versions of your history in your repository. These are called branches. You can use these to work on crazy new ideas in your code, and still keep a branch with your working code you use to do science.

To create a new branch, you can do:

    git branch experiment
    git branch
    
>  experiment
>  * master

The asterisk indicates the branch you are "on". Although you created the `experiment` branch, you're still on the master branch. Switch to the experiment branch with:

    git checkout experiment 

And let the server know there's a new branch with:

    git push experiment

Go ahead and make some changes to files, and commit and push them with `git push`. You'll see that they only appear in the experimental branch. When you want to switch back to your main branch, make sure you're fully commited, with no changes to files waiting to commit, then do:

    git checkout master
    
Now, you can pull your changes back from your experimental branch into the master branch, with

    git merge experiment
    
If you have committed changes on both master and experiment, you may hit conflicts, where git can't work out how to merge them. We'll discuss this in detail later, when we look at collaboration, so for now, ask a demonstrator to help with this.

Git gives you the power to label a particular version of your code with a more readable name. This is called a "tag". This is important for making sure you only do science with a certain version. 

Label your current version with:

    git tag -a v0.2

Pick an old commit using `git log`, and label it like this:

    git tag -a v0.1 c438f17

You can now go back to the v0.1 commit like this:

    git checkout v0.1

and then switch back to the main code with

    git checkout master
    
You can refer to any tagged commit with the tag name, anywhere you would otherwise use a commit hash code, or a HEAD-based reference.

You need to push your tag labels up to the remote, with

    git push --tags
                      
You should now be able to see these under tags, in the dropdown menu on the left. 

5. GitHub pages
---------------

GitHub will publish repositories containing markdown as web pages, automatically. You can do this by creating a branch called `gh-pages`. You'll need to add this content:

    ---
    ---

A pair of lines with three dashes, to the top of each markdown file. 
[Here's why](https://github.com/mojombo/jekyll/wiki/YAML-Front-Matter) for the curious. 

And then add a special named branch, which GitHub uses to create a website for any repository. This is best used to create documentation for a program you write, but you can use it for anything:

    git branch gh-pages
    git checkout gh-pages
    git push origin gh-pages
    
The first time you do this, GitHub takes a few minutes to generate your pages. The website will appear at `http://username.github.com/repositoryname`, for example, here's mine: http://jamespjh.github.com/jh-ucl-swcarpentry-answers/     

You can use this syntax

    [link text](URL)
    
To create hyperlinks in your pages, so you can link between your documents. Try it! If you want, after the class, to see how to make pretty HTML layouts for github pages, see http://github.com/UCL/ucl-github-pages-example, which displays at http://ucl.github.com/ucl-github-pages-example.

6. Collaboration
------------------------
