#!/usr/bin/env python3
import psycopg2


# What are the most popular three articles of all time?
query1_title = ("What are the most popular three articles of all time?")
query1 = (
    "select articles.title, count(*) as views "
    "from articles inner join log on log.path "
    "like concat('%', articles.slug, '%') "
    "where log.status like '%200%' group by "
    "articles.title, log.path order by views desc limit 3")

# Who are the most popular article authors of all time?
query2_title = ("Who are the most popular article authors of all time?")
query2 = (
    "select authors.name, count(*) as popularity from articles inner "
    "join authors on articles.author = authors.id inner join log "
    "on log.path like concat('%', articles.slug, '%') where "
    "log.status like '%200%' group "
    "by authors.name order by popularity desc")

# On which days did more than 1% of requests lead to errors
query3_title = ("On which days did more than 1% of requests lead to errors?")
query3 = (
    "select day, percentage from ("
    "select day, round((sum(requests)/(select count(*) from log where "
    "substring(cast(log.time as text), 0, 11) = day) * 100), 2) as "
    "percentage from (select substring(cast(log.time as text), 0, 11) as day, "
    "count(*) as requests from log where status like '%404%' group by day)"
    "as log_percentage group by day order by percentage desc) as final_query "
    "where percentage >= 1")


def connect(dbname="news"):
    """Connect to the PostgreSQL database. Returns a database connection """
    try:
        db = psycopg2.connect("dbname=news")
        cursor = db.cursor()
        return db, cursor
    except:
        print ("Unable to connect to the database")


def get_query_results(query):
    """Return query results for given query """
    db, cursor = connect()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()


def print_query_results(query_results):
    print (query_results[1])
    for index, results in enumerate(query_results[0]):
        print (
            "\t", index+1, "-", results[0],
            "\t - ", str(results[1]), "views")


def print_error_results(query_results):
    print (query_results[1])
    for results in query_results[0]:
        print ("\t", results[0], "-", str(results[1]) + "% errors")


if __name__ == '__main__':
    # store query results
    popular_articles_results = get_query_results(query1), query1_title
    popular_authors_results = get_query_results(query2), query2_title
    load_error_days = get_query_results(query3), query3_title

    # print query results
    print_query_results(popular_articles_results)
    print_query_results(popular_authors_results)
    print_error_results(load_error_days)
