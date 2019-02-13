# logs-analysis-project
## by Shannon Tjang

Internal reporting tool that leverages database information to figure out what kind of articles the site's readers like. Project in fulfillment of the [Udacity Full Stack Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).



## Prerequisites
You have installed the following programs
```
Python
psycopg2 2.7.3.2
PostgreSQL 9.5.10
```
Generally any recent version of Python will do, as Python makes every attempt to maintain backwards compatibility.


## Contents
`newsdata.zip` - a zipped file containing the `newsdata.sql` file that populates the news PostgreSQL database
`README.md` - Read me!
`logsanalysis.py` - a python module that uses database information of a web server (`newsdata.sql`) to conclude visitor activity on the site. The database includes three tables:
  1. articles - a list of articles on the site;
  2. authors - information about the authors of articles;
  3. log - each time a visitor has accessed the site

# Instructions

Launch your preferred Linux-based Shell terminal.

## Initialize your Virtual machine

```
vagrant up
```
This command downloads the Linux operating system and installs it on first initialize. If you already have Vagrant installed, this takes your virtual machine online.

```
vagrant ssh
```
This command logs you into the vagrant system.

Next clone the repository to your local machine with the following command:
```
git clone <https://github.com/shannonymous/logs-analysis-project>.
```
Ensure that this file is put into the vagrant directory, which is shared with your virtual machine.

To load the data, `cd` into the vagrant directory with `cd /vagrant`.

We will then need to run the following commands to load up our newsdata database:
  1. `unzip newsdata.zip`
  2. `psql -d news -f newsdata.sql`

## Running queries
The logsanalysis.py file contains all necessary to execute and answer the three questions posted in the project. To run, execute the following command:
```
python logsanalysis.py
```

## Output
Your output should return the same results as in the `output.txt` file.



## Shut Down
After running `logsanalysis`, you can exit psql by entering `Command-D` (or `Ctrl-D`). You can shutdown vagrant with the following command
```
vagrant halt
```
