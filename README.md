# ddsv
A simple python package to manage default-delimiter-separated value (DDSV) files. 

## Example
```
>>> import ddsv
>>> a = [1, 2, 3]
>>> ddsv.dump(a, "filename.txt")
>>> data = ddsv.load("filename.txt")
>>> data
[1, 2, 3]
>>>
```
