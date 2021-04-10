git help : to check different available commands with git

git help cmd-name : to check the documentation, usage of a selected command

command  	  				| usage
------------- 				| -------------
git init  					| Navigate to a folder in your local machine, and run the command to initialize git in that folder
git status  				| It will check call the files in git repository (the folder where the git initialized)
git add  					| Add file to staging area then we can commit it
git add --all 				| Add all files to staging area
git rm --cached filename    | remove a file from staging area, this will become un-tracked again
git rm --cached *			| remove all file from staging area
git commit 					| will save all staged changes, along with a brief description from the user, in a “commit” to the local repository. git commit is like a snapshot of your project. you can recall the commit or revert changes later. git commit will commit all staged files with their changes, if you dont want apply commit on a particular file, you have to unstage the file first.
git commit -m "message" 	| commit the staged files, by default it will launch a text editor where you need to type your commit message
git commit -a -m "message" 	| commit all the staged files but it only includes the tracked files ( means the files the added with git add command)
git remote add origin remote-url | add a remote to your local repository, origin is default short name for the new remote you created.
git remote -v 				| Verify that remote is added to your local repo , it will show a shortname and its remote URL where it is mapped to
git remote add second remote-url | You can add more remotes to the same Git repo by specifying a different shortname for the new remote
git push -u origin master 	| it will update state of your remote repo "origin" to the same state of the local repo
git push -u second master 	| it will update state of your remote repo "second" to the same state of the local repo


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
