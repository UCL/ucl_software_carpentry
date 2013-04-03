UCL Git and GitHub training
===========================

In this module, you will learn how to manage your code with Version Control. This will allow you to see the history of your code, roll back mistakes, to collaborate smoothly with other people on the same code, and to publish your code to the internet for other people to use.

This course will use the `git` version control system, but much of what you learn will be valid with other version control tools you may encounter, including subversion (`svn`) and mercurial (`hg`).

In this course, we will use, as an example, the development of a few text files containing a description of a topic of your choice. This could be your research, a hobby of yours, or something else. In the end, we will show you how to display the content of these files as a very simple website. The text files we create will use a simple "wiki" markup style called [markdown](http://daringfireball.net/projects/markdown/basics) to show formatting. This is the convention used in this file, too. You can view the content of this file in the way Markdown renders it by looking on the [web](https://github.com/UCL/ucl_software_carpentry/blob/master/git/git_instructions.md), and see compare the [raw text](https://raw.github.com/UCL/ucl_software_carpentry/master/git/git_instructions.md).

The purpose of this exercise is to learn how to use Git to manage program code you write, not simple text website content, but we'll just use these text files instead of code for now, so as not to confuse matters with trying to learn version control while thinking about programming too. On the second day of the bootcamp, you should use the version control tools you learn today as you work on that day's exercises. 

1. Solo work
--------------------

This is an alternative version of the instruction materials that uses the Windows or Mac Github GUI instead of the command line. You'll need to sign up for a GitHub account at [GitHub](https://github.com/), fill in a username and password, and click on "sign up for free". Then, download the client, from http://mac.github.com/ or http://windows.github.com/, and fill in your details. 

Create a folder to do your work in, using the Finder on mac or Explorer on Windows, then hit "add" in the gui, uncheck "push to github", and choose a location, name, and description.

Hit the arrow to open the repo. It contains some default files.

We're going to add a new file via the finder or explorer, then edit it with notepad. Choose "tools" then "open in explorer (or finder)" Use explorer or finder to create a new file called "index.md" (Not index.md.txt: if you've got explorer set to hide file extensions, you won't be able to use "new text file") 

Edit the file to contain your desired content. Then commit your change using the box in the corner of the window, with a commit message and a description.
 
And note the confirmation: the commit appears as an "unsynced commit" on the right hand side. 

Make another change to the file, this time with a mistake

Note that the change now appears as an "uncommitted change," showing the differences in the file.

Commit the change.

Now two commits appear as "unsynced commits".

Great, we now have a file which contains a mistake.

In a while, we'll use Git to roll back to the last correct version: this is one of the main reasons we wanted to use version control, after all! But for now, let's do just as we would if we were writing code, not notice our mistake and keep working...

Make a third change.

We now have three changes in the unsynced commits.
 
2. Fixing Mistakes
------------------
 
Ok, so now we'd like to undo the nasty commit with the lie about Mount Fictional.

Click on this commit. Notice the "roll back this commit" and "revert commit" buttons. Choose "revert commit". (If you get a warning about a conflict, ask your demonstrator for help.)

Notice how the mistake has stayed in the history: you can see a commit which undoes the change: this is colloquially called an "antipatch". This is nice: you have a record of the full story, including the mistake and its correction.

It is possible, in git, to remove the most recent change altogether, "rewriting history". Make another bad change, of your choice, by editing the file, and committing again. 

Now, click on the commit, and then on "roll back this commit"

The silly spelling is gone, and *it isn't even in the list of commits*. This approach to fixing mistakes, "rewriting history" with `reset`, instead of adding an antipatch with `revert` is dangerous, and we don't recommend it. But you may want to do it for small silly mistakes, such as to correct a commit message.

When git reset removes commits, it leaves your working directory unchanged -- so you can see the bad commit is now a new commit ready to be included. To fully get rid of the bad change, right click the file, and choose "discard changes."
    

3. Publishing
---------------------

So far, all our work has been on our own computer. But a big part of the point of version control is keeping your work safe, on remote servers. In this example, we'll be using the "GitHub" cloud repository to store our work. 


Ok, let's create a repository to store our work. Hit "push to github" on the top of the window.

For this software carpentry course, you should use public repositories in your personal account for your example work: it's good to share, so don't click "keep this code private". GitHub is free for open source, but in general, charges a fee if you want to keep your work private. In the future, you might want to keep your work on GitHub private: students can get free private repositories on GitHub, by going to [https://github.com/edu] and filling in a form. UCL Research Software Development can support your research group with the cost of private repositories if you need it: get in touch at rc-softdev@ucl.ac.uk for more details.

This sets up the server on github as a "remote", called "origin". Git, unlike some earlier version control systems is a "distributed" version control system, which means you can work with multiple remote servers. Usually, commands that work with remotes allow you to specify the remote to use, but assume the "origin" server if you don't. 

Now, hit "publish to github". Now you'll be able to see it on the internet! Click on the icon indicating "GitHub", and the repository will open in your browser.

Take a few moments to click around and work your way through the GitHub interface. Try clicking on 'index.md' to see the content of the file: notice how the markdown renders prettily.

Click on "commits" near the top of the screen, to see all the changes you've made. Click on the commit number next to the right of a change, to see what changes it includes: removals are shown in red, and additions in green.

Let's make some more changes, and see how to publish them to GitHub as we go.

4. Multiple files
------------------------

So far, we've only worked with one file. Add another with your editor, put some content in it. Make some changes to the first file too.

Note you can use checkboxes to decide which files to include in your next commit. You could do both files together, or two commits with changes to one file in each commit. It's up to you.

Your change is on your local copy, but won't hit GitHub until you hit "sync". Hit "sync" to push your changes to github. Visit GitHub, and notice this change is on your repository on the server.

Note that you can also make changes in the GitHub website itself. Visit one of your files, and hit "edit. This will not work in IE 7 or 8, so you can only try this next bit if you're using IE 9 or another browser.

Make a change in the edit window, and add an appropriate commit message.

That change now appears on the website, but not in your local copy. (Verify this). To get the change into your local copy, hit "sync" and check the change is now present on your local version. `git pull` will fetch changes on the server into your local copy: this is important when you are collaborating with others, as we shall see.
 
5. Branching and tagging
------------------------

Git lets you maintain different versions of your history in your repository. These are called branches. You can use these to work on crazy new ideas in your code, and still keep a branch with your working code you use to do science.

To create a new branch, you should click on the trident symbol. In the "filter or create new" box, type "experiment", and choose "create new branch experiment"

The name next to the trident indicates the branch you are "on". Stay on the experiment branch for now.

Make a change, and commit it. The change is in your file, but if you switch to the master branch, it won't be.

    git checkout master
    
You'll need to publish your changes from the experiment branch. Verify the branch appears on the github website. Now, you can pull your changes back from your experimental branch into the master branch,  by choosing "manage" on the branches dropdown. Drag your branches into the merge window, and observe the results. 
    
If you have committed changes on both master and experiment, you may hit conflicts, where git can't work out how to merge them. We'll discuss this in detail later, when we look at collaboration, so for now, ask a demonstrator to help with this.          

You'll need to publish the results of your merging, using "sync".

Git also gives you the power to label a particular version of your code with a more readable name. This is called a "tag". Currently, this isn't possible using the GUI.

6. GitHub pages
---------------

GitHub will publish repositories containing markdown as web pages, automatically. You can do this by creating a branch called `gh-pages`. You'll need to add this content:

    ---
    ---

A pair of lines with three dashes, to the top of each markdown file. 
[Here's why](https://github.com/mojombo/jekyll/wiki/YAML-Front-Matter) for the curious. 

And then add a special named branch, which GitHub uses to create a website for any repository. This is best used to create documentation for a program you write, but you can use it for anything. The special branch should be called gh-pages.

The first time you do this, GitHub takes a few minutes to generate your pages. The website will appear at `http://username.github.com/repositoryname`, for example, here's mine: http://jamespjh.github.com/jh-ucl-swcarpentry-answers/     

You can use this syntax

    [link text](URL)
    
To create hyperlinks in your pages, so you can link between your documents. Try it! If you want, after the class, to see how to make pretty HTML layouts for github pages, see http://github.com/UCL/ucl-github-pages-example, which displays at http://ucl.github.com/ucl-github-pages-example.

7. Collaboration
------------------------

Now we're going to get to the most important question of all with Git and GitHub: working with others.

Organise into pairs. You're going to be working on the website of one of the two of you, together, so decide who is going to be the leader, and who the collaborator.
 
Next, the leader needs to let the collaborator have the right to make changes to his code.

In GitHub, go to `settings` on the right, then `collaborators` on the left.

Add the user name of your collaborator to the box. They now have the right to push to your repository.

Next, the collaborator needs to get a copy of the leader's code. Go to the collaborator's page, then choose "clone in windows." The repository will appear as another repository in your github client.

Now, both of you should make some changes. To start with, make changes to *different* files. Both of you should commit, but not publish. This will mean your work doesn't "conflict". Later, we'll see how to deal with changes to a shared file.

One of you should now sync.

The other should then sync, notice you now have both sets of changes.

Go through the whole process again, but this time, both of you should make changes to a single file, but make sure that you don't touch the same *line*. Again, the merge should work as before.

Finally, go through the process again, but this time, make changes which include changes to a shared line.

There's a big scary error message:

> failed to sync this branch due to unmerged files.  

GitHub couldn't work out how to merge the two different sets of changes. The program offers to open a command line for you. You'll need this to mark your change as resolved. Edit the file to manually resolve the conflict.

>     <<<<<<< HEAD  
>     Wales is hillier than England, but not quite as hilly as Scotland.  
>     =======  
>     Wales is much hillier than England, but not as hilly as Scotland.  
>     >>>>>>> dba9bbf3bcab1008b4d59342392cc70890aaf8e6  

The syntax with `<<<` `===` and `>>>` shows the differences between the files. You can get editors which can understand this syntax and make it easy to merge, but for now, just manually edit the file, to combine the changes and get rid of the symbols.

> Wales is much hillier than England, but not quite as hilly as Scotland. 

Now commit the merged result in the command line:

    git commit -a      
    
A suggested commit message appears, which you can accept, and then you can push the merged result. Sync in the gui, then check everything is fine on GitHub.

8. Social Coding
----------------

In addition to being a repository for code, and a way to publish code, GitHub is a social network.  You can follow the public work of other coders: go to the profile of your collaborator in your browser, and it the "follow" button. 

Here's mine: https://github.com/jamespjh : if you want to you can follow me.

Using GitHub to build up a good public profile of software projects you've worked on is great for your CV!

9. Pull Requests
----------------

If you want to collaborate with someone, but you don't want to give them the right to change your code directly, you can collaborate through *pull requests* instead of by granting them access.

Swap roles. This time, the collaborator, instead of pulling the principal's code, should *fork* it. Go to the repository on GitHub, and hit "fork" top right.

A new repository will be created on the collaborator's account, which contains all the same stuff. The new collaborator should hit "clone in windows" to get a copy of this.

Both of you can make changes. (Make them to different files now for simplicity.) Now, both of you will be able to push: you're pushing to different repositories!
 
You need to request that the leader accept your changes. The collaborator should go to the page for their *forked* repository and hit "pull request", and then choose the right branches and repositories for the "base", the leader's repository, and the "head repo", the collaborator's repository. Ask a demonstrator for help if this is confusing. 

Give the request a title and a comment, and send it.  

The leader should now see a link to the pull request on their github home page. Check it out, and if you think its fine, then merge it, using the big green button. (If there's a conflict, there won't be a big green button: ask your demonstrator for help with how to merge a conflicted pull request.) 

Note you can comment on and discuss the contribution using the pull request: this is great for open source projects with many people working together.

