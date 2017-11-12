# UTF-8 Fixer

These scripts allow you to fix the encoding problem that is created when a characters with UTF-8 encoding are decoded with another encoding and then stored as (or converted to) an UTF-8 encoded string, again.

A typical examples that illustrate this problems would be strings ended up looking like "niĂąos, mĂĄs certificaciĂłn" instead of "niños, más certificación" (see more examples in folder example/files/).


## Description of files:
* **utf8fixer-bruteforce.py**: this script takes a file path as command line argument an generates a copy of it for each encoding available. Note: if the file is called "thefile.txt", each copy is going to be named as "thefile_ENCODING.txt", where ENCODING is the actual encoding used to fix the file encoding. This is useful to find out what the correct encoding should be. An example is: ```$ python utf8fixer-bruteforce.py example/bruteforce/file0.txt```, then we should check each created file to find out what the correct encoding is (in case of this example, the correct one is "iso8859_2"). Once we've done that, we can use one of the following two files, according to our needs.

* **utf8fixer.py**: this script takes a file or a dir path as a command line argument, as well as, optionally, the correct encoding and/or whether to also normalize the unicode characters (i.e. convert characters like á,é,í,ó,ú,ñ,etc. to a,e,i,o,u,n, etc. respectively). For example: ```$ python utf8fixer.py example/files/``` will fix all the files in example/files using the default encoding which is "iso8859_2".

* **import-example.py**: an example script that imports the ```fix_encoding```function to fix the encoding. This is useful when the files have mixed encoding, for instance a structured file such as an xml, in which only certain elements are badly encoded, then you could use this function to iterate over each element and fix each one separately.
