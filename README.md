# python-task

codingtest.py <file_name> <sum|avg|median> [<gt|lt|eq> <n>]
  
Where [<gt|lt|eq> <n>] are optional arguments. Test file "testfile.txt" is provided in the repo.

Example executions:
```
$ py codingtest.py testfile.txt median gt 500
Median is:  444.0
444.0  is not greater than  500.0
$ py codingtest.py testfile.txt sum
Sum is:  59717.0
```

Tested working on python 3.8.1, Windows 10
