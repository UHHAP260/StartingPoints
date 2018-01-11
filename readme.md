readme.med for A260_UHH18S

Experiment in using git and GitHub to maintain a few files for the ASTR/PHYS260 class for Spring 2018.


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
git commit -a  # will add and commit in one step any modified file but not new ones
git log 
git mv readme.txt readme.md  #renamed the file
git status
git commit -m "Changed readme from .txt to .md"
```

Do this to clone the MkPy materials:

```
git clone qpython-tutorial.git
cd python-tutorial
git pull. # update to the latest
```

References for Git
-------------------
```
man git
man gittutorial
man giteveryday
```
[git website](https://git-scm.com)

