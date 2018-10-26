# udacity-logs-analysis
Script code for a website logs analysis.

Script Design
=============
This script depends on **psycopg2** for connecting to the database and and apply SQL queries to it.
[**psycopg2**](http://initd.org/psycopg/) is a Python library for connecting to and managing PostgreSQL databases. after psycopg2 connects to the database it returns a connection object. And the we use this object to create multiple cursor objects, each cursor represent an SQL query. cursors will hold result sets of its queries after querying, which can be extracted using fetchall() method. finally we use Python code to better format result values.

[**psycopg2**](http://initd.org/psycopg/) python library is required to be installed before starting the project. 

Installation
============
This script works only on Python 3.
you can make a clone of this project with this command

	git clone https://github.com/abu-3abed/udacity-logs-analysis.git
or you can download it manually by pressing 'Clone or download' and then 'Download ZIP'.

after installing project you can install **psycopg2** using pip package manager by entering this in your command line:

	pip3 install psycopg2
	
(note: pip3 is used to grab Python 3 version.)
more information on **psycopg2** Python library in its [documentation](http://initd.org/psycopg/docs/).

starting project
================

after installing the project and psycopg2 you can run the project by running 'news.py' file from cmd or bash. run this command on the project directory:

	python news.py


Happy coding!!
