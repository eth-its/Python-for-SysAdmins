# Python for Sysadmins (2/4)

## Interaction with the file system

### utilities to look around

**most often used: the os module**
**file path as object: the pathlib module**

```
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
```

**match file patterns: glob**

**match file patterns: fnmatch**

### copying and moving files: shutils


### open and close files correctly

**with statement**

- show problems when not using it
- own with statement

**watch out for text-encoding**

**handling JSON files: json**

**handling CSV files: csv and pandas**

- pandas is not standard module, needs to be installed first

**handling XML files: BeautifulSoup 4**

`pip install beautifulsoup4`

Easy walkthrough:

```
soup = BeautifulSoup(unicode_string, 'lxml-xml')
node = soup.find('element')
node.children
node.parents
node.attrs.get('attribute_name')
node.name
```


**reading very large files: mmap**

**compare files: filecmp**

- os.stat()
- linecache (large files)

### writing files

**temporary files: tempfile**

### comparing files and directories

**filecmp**

**dircmp**


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






