git help : to check different available commands with git

git help cmd-name : to check the documentation, usage of a selected command

command  	  				| usage
------------- 				| -------------
git init  					| Navigate to a folder in your local machine, and run the command to initialize git in that folder, this will be called as working directory
git status  				| It will check call the files in git repository (the folder where the git initialized)
git add  					| Add file to staging area then we can commit it
git add --all 				| Add all files to staging area
git commit 					| will save all staged changes, with a message why commit is done. git commit will commit all staged files with their changes, if you dont want apply commit on a particular file, you have to unstage the file first.
git commit -m "message" 	| commit the staged files, by default it will launch a text editor where you need to type your commit message
git commit -a -m "message" 	| commit all the staged files but it only includes the tracked files ( means the files the added with git add command)

**staged (can also think as tracked files) files:**

files which are added and they are ready to commit

color code: GREEN

------------------------------------------------------------
**un-staged files:**

any file that is modified, we need to stage them again to commit

color code: RED

------------------------------------------------------------

**un-tracked files:**

Newly created files, we need to stage them first to commit them 

color code: RED

------------------------------------------------------------

**Git Basic Workflow**

![alt text](https://github.com/rajuatmakuri5/Google-it-automation-python-coursera/blob/main/git%20and%20github%20learning/git_basic_workflow.JPG)
