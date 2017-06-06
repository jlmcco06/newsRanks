# NewsRanks

NewsRanks is a reporting tool which operates on the **news** database, and does the following:

* Provides the titles and  number of user views for the three most popular articles in the database

* Lists and ranks all of the authors in the database, and counts the number of users who have attempted to view their articles.

* Finds and reports any days in the database during which more than 1% of user requests for articles resulted in an error.  

## Requirements

* Python 2 or later
* psycopg2

## Instillation

**Clone** the **NewsRanks** repository from `https://github.com/jlmcco06/newsRanks.git` using terminal or commandline.

When repository has been cloned, the following files should be present:

* **README.md** - You're reading this!

* **newsranks.py** - Reporting tool

## Running Reports

**Important!!!**

Before running the the python code, you must first access the database by entering `psql news`into your terminal. This will ensure that all of the necessary views are present. Enter the following code into your terminal:

`CREATE OR REPLACE VIEW errors as 
SELECT date(time),
COUNT(status) as failures
FROM log
WHERE status like '%404%'
GROUP BY date(time)
ORDER BY date(time);`

Then

`CREATE OR REPLACE VIEW requests as
SELECT date(time),
COUNT(status) as attempts
FROM log
GROUP BY date(time)
ORDER BY date(time);`

The first will create a view called **errors** which produces a view counting the number of errors on each day. The second produces a view called **requests** which counts the total number of user requests per day. The **newsranks.py** code will need these views for calculations.

Once these views have been added or replaced, type `python newsranks.py` into your terminal or command line.

That's It! Your terminal should display NewsRanks' output!  
