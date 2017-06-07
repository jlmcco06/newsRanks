#!/usr/bin/env python2.7
import psycopg2


def top_three():
    """Query returning top three articles in database ranked by
    number of times users accessed article"""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("SELECT articles.title, COUNT(log.path) as popularity \
    	FROM articles JOIN log ON (articles.slug = (substring(log.path, \
            10))) GROUP BY articles.title ORDER BY popularity DESC LIMIT 3")
    tops = c.fetchall()
    db.close()
    print "\nMost popular articles:\n"
    for article in tops:
        print str(article[0]) + " - " + str(article[1]) + " views"


def rank_authors():
    """Query returning most popular authors based on munber of \
    users who accessed articles written by each author"""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("SELECT authors.name,COUNT(log.path) as popularity \
        FROM authors JOIN articles ON (authors.id = articles.author) JOIN \
        log ON (articles.slug = (substring(log.path, 10))) GROUP BY \
        authors.name ORDER BY popularity DESC")
    ranks = c.fetchall()
    db.close()
    print "\nMost popular authors:\n"
    for author in ranks:
        print author[0] + " - " + str(author[1])


def fails_over_one_percent():
    """Query returning dates on which more than 1% of requests failed"""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("SELECT errors.date, (1.0 * errors.failures/ \
        requests.attempts) * 100 as percent_fails FROM errors \
    INNER JOIN requests ON (errors.date = requests.date) WHERE \
    (1.0*errors.failures/ requests.attempts) * 100 > 1.0")
    above1 = c.fetchall()
    db.close()
    print "\nDays with more than 1% errors:\n"
    for day in above1:
        print str(day[0]) + ", rate- " + str(round(day[1], 2)) + "%"

top_three()
rank_authors()
fails_over_one_percent()
