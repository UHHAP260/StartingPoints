UHHAP260/StartingPoints
=======================

We're experimenting with git and GitHub to maintain files for the ASTR/PHYS260 class for Spring 2018. 
This readme.md file contains instructions on [how to download materials from this repossitory to your computer](#instructions), 
a [record of git and GitHub commands and used to set up the repository](#setup), 
and [references for git and GitHub](#references).

Downloading this GitHub Project to Your Computer <a id="instructions"></a>
---------------------------------------------------

1. Make sure that you have git installed on your computer: (from a terminal)
    ```
    git --version
    ```
1. If not install git (see references below)
1. Configure git with your name and email.
    ```
    git config --global user.name "First Name Last Name"
    git config --global user.email you@yourdomain.example.com
    ```
1. __cd__ into the directory into which you want to pull (import) the StartingPoints repository/directory and issue the commands

    ```
    git clone https://github.com/UHHAP260/StartingPoints.git
    ```
1. You have two options for editing and creating your own versions of these files to edit. 

    1. If you are ready to become familiar with git, make your own branch of the directory so you can play around with it. 
    (Use your own branch name for "my-branch")   
    ```
    cd StartingPoints
    git branch my-branch
    git checkout my-branch
    ```    
    2. Create another directory into which you can create copies of specific files 
    in the StartingPoints repository that you want to edit.


1. When you want to get updated materials, go back to the 'StartingPoints' directory on your computer and 'pull' the new material. 
 
    ```
    git pull
    ```
    I haven't tried this yet, but if you've created your own branch to work in. You may need to try this instead:
    
    ```
    git checkout master
    git pull
    git checkout my-branch
    git merge master
        ```
1. This is all you need to know for using git to stay current with resource material.

Basic Commands for Getting Started with Git <a id="setup"></a>
-------------------------------------------

To get started, I needted to tell git who I am:

```
git config --global user.name "Your Name Comes Here"
git config --global user.email you@yourdomain.example.com
```

Commands used are:

```
mkdir directory
cd directory
git init
git add readme.txt
git add .  # this would add everything
git commit -m "brief summary of actions"
git commit -a "bried summary of actions"  # will add and commit in one step any modified file but not new ones
git log 
git mv readme.txt readme.md  #renamed the file
git status
git commit -m "Changed readme from .txt to .md"
```

Do this to clone the MkPy materials:

```
git clone https://github.com/MkPy/python-tutorial.git
cd python-tutorial
```

This is what I had to do to put the materials I had on my computer onto GitHub 
once I created an account and created the organization UHHAP260 and started the repository
"StartingPoints."

```
git remote add origin https://github.com/UHHAP260/StartingPoints.git
git push -u origin master
```

References for Git and GitHub <a id="references"></a>
-----------------------------

- from the terminal you can use the commands:

    ```
    man git
    man gittutorial
    man giteveryday
```
- [git website](https://git-scm.com)
- [a really basic tutorial](http://rogerdudler.github.io/git-guide/)
