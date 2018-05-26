# Recursive Crawl

## Description

This crawler recursively visits links specified in the href field of <a> tag of an html file and outputs parsed text into separate files. The list of visited URLs is recorded in the URL.txt file.

Root page: http://cspro.sogang.ac.kr/~gr120170213

## How-to

This is a project worked in python3 virtual environment. Aside from all default modules included when creating virtual environment with **virtualenv** command, following modules are also included:
* requests
* beautifulsoup4

So, to execute this crawler, do the following:
1. Download project
(Optional: remove all *.txt files for fresh start)
2. Start virtual environment with following command:
```
(from the project's root directory)
$ . ./bin/activate
```
3. Run python script:
```
$ python3 20161577.py
```
4. Crawl result files are created in project's root directory.
5. Deactivate virtual environment:
```
$ deactivate
```
