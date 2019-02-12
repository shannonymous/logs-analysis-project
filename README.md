# logs-analysis-project
## by Shannon Tjang
Internal reporting tool that will use information from the database to discover what kind of articles the site's readers like. Project in fulfillment of the [Udacity Full Stack Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).



## Prerequisites
You have installed the following programmes
```
Python 3.5.2
psycopg2 2.7.3.2
PostgreSQL 9.5.10
```


## Contents
`logsanalysis` is a python module that uses database information of a web server to conclude visitor activity on the site. The database includes three tables:
  1. articles - a list of articles on the site;
  2. authors - information about the authors of articles;
  3. log - each time a visitor has accessed the site
