Git log command helps to navigate through all changes happened to Git repo.
we can review everything that happens to Git repo.
It generally display a list of commits and each commit line have below info:

1. 40 character checksum Hash value calculated by SHA, Git use this to maintain consistency and integrity of changes 
2. commit author information
3. date
4. commit message.


command  	  				| usage
------------- 				| -------------
git log						| it will list all recent commits , u can add option --all to list all commits 
git log -p 					| This is patch command display the files that have been modified, it the location where new lines added, removed or updated. This is very simliar to diff -p command.
git log --oneline			| It will display very minimum information in single line for each commit
git log graph 				| Git log command allows viewing your git log as a graph. you can add --oneline option to see one line at a time.
git log --after="yy-mm-dd"  | after a given date
git log --after="20 days ago" 
git log --after="yy-mm-dd" --before="yy-mm-dd"\
git log --author			| based on author name
