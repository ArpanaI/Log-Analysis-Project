Logs Analysis

By Arpana Ijantkar

About

In this project, a large database with over a million rows is explored by building complex SQL queries to draw business conclusions for the data. The project mimics building an internal reporting tool for a newpaper site to discover what kind of articles the site's readers like. The database contains newspaper articles, as well as the web server log for the site.

To Run

You will need:

Python3
Vagrant
VirtualBox Setup

Install Vagrant And VirtualBox

Launch Vagrant VM by running vagrant up, you can then log in with vagrant ssh

To load the data, use the command psql -d news -f newsdata.sql to connect a database and run the necessary SQL statements.

The database includes three tables:

Authors table
Contains Columns(name, bio, id)

Articles table
Contains Columns(author, title, slug, lead, body, time, id)

Log table
Contains Columns(path,ip,method,status,time,id)

To execute the program, run python3 newsData.py from the command line.