# Python for Sysadmins (2/4)

## Interaction with the file system

### open and close files 

### binary, text, encoding

### JSON files

### CSV files, pandas

- pathlib instead of os.path: http://proquest.safaribooksonline.com/book/programming/python/9780134291154/chapter-6dot-the-file-system/ch06lev1sec2_html?uicode=ETH
- os.listdir()
- glob
- fnmatch
- os.stat()
- linecache (large files)
- tempfile
- filecmp
In [5]: usr = pathlib.PurePosixPath('/usr')                                                                                                                                                                                                                 

In [6]: usr                                                                                                                                                                                                                                                 
Out[6]: PurePosixPath('/usr')

In [7]: print(usr)                                                                                                                                                                                                                                          
/usr

In [11]: usr_local = usr / 'local'                                                                                                                                                                                                                          

In [12]: usr_local                                                                                                                                                                                                                                          
Out[12]: PurePosixPath('/usr/local')

In [13]: usr_local.as_posix()                                                                                                                                                                                                                               
Out[13]: '/usr/local'

In [14]: usr_local.as_uri()                                                                                                                                                                                                                                 
Out[14]: 'file:///usr/local'







## Interaction with the shell

### execute commands

### pipe output to the next command

### execute ssh calls



## REST API

### The request module

### handling of errors



## useful modules

https://docs.python-guide.org/scenarios/admin/


### datetime
### re: regular expressions
### atexit: execute when things fail
### copy
### sqlite3
### fabric: https://docs.fabfile.org/en/2.5/

### Psutil
Psutil is an interface to different system information (e.g. CPU, memory, disks, network, users, and processes).
https://github.com/giampaolo/psutil/

### Ansible




