# Logs analysis project for Udacity Fullstack nanodegree
import psycopg2

DBNAME = "news"


def connect():
    try:
        #connect to the db
        conn = psycopg2.connect(database=DBNAME)
        c = conn.cursor()
    except:
        print("Unable to connect to the database.")
        return None
    else:
        return c

print("")
print('Udacity Logs Analysis Project Answers')
print("====================================================")

#Question 1: What are the most popular three articles of all time?
def three_most_popular_articles(cursor):
#Gets the all time top three articles by popularity
    question = """
        SELECT articles.title, count(*) as num
        FROM articles, log
        WHERE '/article/' || articles.slug = log.path
        GROUP by articles.title
        ORDER by num desc
        LIMIT 3;
    """
    cursor.execute(question)
    results = cursor.fetchall()

#This section prints the results via loop:
    print ('1. The three most popular articles of all time are:')
    for result in results:
        print ('    "{title}" - {num} views'
        .format(title=result[0], num=result[1]))


#Question 2: Who are the most popular article authors of all time?
def author_by_popularity(cursor):
    #Ranks the most popular authors by total views
    question = """
        SELECT authors.name, count (*) as num
        from authors, articles, log
        where '/article/' || articles.slug = log.path
        AND articles.author = authors.id
        group by authors.name
        order by num desc;
    """
    cursor.execute(question)
    results = cursor.fetchall()

#This section prints the results via loop:
    print("")
    print("")
    print ('2.The most popular authors of all time are:')
    for result in results:
        print ('    {author} - {num} views'
        .format(author=result[0], num=result[1]))


#Question 3: On which days did more than 1% of requests lead to errors?
def more_than_1_pc_error(cursor):
    #Returns the days where error rate is more than 1% in a list
    question = """
        WITH daily_requests as(
            SELECT count(log.status) as num, cast(log.time as date) as date
            from log
            group by date
        ), daily_errors as(
            select count(log.status) as num, cast(log.time as date) as date
            from log
            where status like '404%'
            group by date
        ), error_rate as(
            select daily_requests.date, (daily_errors.num::float / daily_requests.num::float) * 100 as percent_error
            from daily_requests, daily_errors
            where daily_requests.date = daily_errors.date
        ) select * from error_rate where percent_error > 1;
    """
    cursor.execute(question)
    results = cursor.fetchall()

#This section prints the results via loop:
    print("")
    print("")
    print ('3. The days when more than 1% of requests led to errors are:')
    for result in results:
        print('    {time:%B %d, %Y} - {percent_error:.1f}% errors'.format(
            time=result[0],
            percent_error=result[1]))

    print("")


if __name__ == "__main__":
    cursor = connect()
    if cursor:
        three_most_popular_articles(cursor)
        author_by_popularity(cursor)
        more_than_1_pc_error(cursor)
        cursor.close()
