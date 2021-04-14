**Open Function**

Open file and return a corresponding file object. If the file cannot be opened, an OSError is raised. 
function returns a file object which can used to read, write and modify the file.
if file not found, it will raise FileNotFoundError.

| Character      | Meaning |
| ----------- 	 | ----------- 						|
| 'r'	     	 | open for reading (default)       |
| 'w' 		   	 | open for writing, truncating the file first |
| 'x'			 | open for exclusive creation, failing if the file already exists |
| 'a'            | open for writing, appending to the end of the file if it exists |
| 'b'            | binary mode |
| 't'            | text mode (default) |
| '+'            | open for updating (reading and writing) |

**Syntax:**

open(file, mode)

we can pass additional parameters as required. These are optional parameters.

buffering  - used for setting buffering policy

encoding  - the encoding format

errors  - string specifying how to handle encoding/decoding errors

newline  - how newlines mode works (available values: None, ' ', '\n', 'r', and '\r\n'

closefd  - must be True (default); if given otherwise, an exception will be raised

opener  - a custom opener; must return an open file descriptor

****************************************************************************************************************

File object provide us different methods which help us to read, write, modify the file.

readline()   read oneline at a time.

read()       read from the point where the cursor is in file and read till the end of the file.

readlines()  returns the list of lines in the given file.

write()	     Writes the specified string to the file

writelines() Writes a list of strings to the file
