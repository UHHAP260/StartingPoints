UHHAP260/StartingPoints
=======================

We're experimenting with git and GitHub to maintain files for the ASTR/PHYS260 class for Spring 2018. 
This readme.md file contains a record of git and GitHub commands and resources needed to set up and use this GitHub project.

Downloading this GiHub Project to Your Computer
---------------------------------------------------

1. Make sure that you have git installed on your computer: (from a terminal)
    ```
    git --version
    ```
2. If not install git (see references below)
3. Configure git with your name and email.
    ```
    git config --global user.name "Your Name Comes Here"
    git config --global user.email you@yourdomain.example.com
    ```
4. Create a directory into which you want to download class material.
5. __cd__ into that directory and issue the commands
    ```
    git clone https://github.com/UHHAP260/StartingPoints.git
    ```
6. Make your branch of the directory so you can play around with it. (Use your own branch name for "my-branch")
    
    ```
    cd StartingPoints
    git branch my-branch
    git checkout my-branch
    ```
    
7. At this point you should be able to play around with the material without affecting other people accessing the same project.
8. When you want to get updated materials, go back to 'StartingPoints' and 'pull' the new material. 
 
    ```
    git pull
    ```
9. This is all you need to know for using git to stay current with resource material.

Basic Commands for Getting Started with Git
-------------------------------------------

To get started, I needted to tell git who I am:

```
git config --global user.name "Your Name Comes Here"
git config --global user.email you@yourdomain.example.com
```

Commands used are:

```
mkdir $directory
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
git pull # update to the latest
```
This is what I had to do to put the materials I had on my computer onto GitHub 
once I created an account and created the organization UHHAP260 and started the repository
"StartingPoints."
```
git remote add origin https://github.com/UHHAP260/StartingPoints.git
git push -u origin master
```

References for Git
-------------------

- from the terminal you can use the commands:
```
man git
man gittutorial
man giteveryday
```
- [git website](https://git-scm.com)

