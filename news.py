#!/usr/bin/env python3

import psycopg2


def main():
    conn = psycopg2.connect("dbname=news")

    first_cursor = conn.cursor()
    second_cursor = conn.cursor()
    third_cursor = conn.cursor()
    """first query"""
    print("1. What are the most popular three articles of all time?")

    first_cursor.execute(
        "SELECT articles.title, COUNT(*) FROM articles JOIN log ON log.path = CONCAT('/article/', articles.slug) WHERE log.status = '200 OK' GROUP BY articles.title ORDER BY COUNT(*) DESC LIMIT 3;")
    result1 = first_cursor.fetchall()

    print()
    print("Answer: ")
    print()
    for row in result1:
        print("- \"" + row[0] + "\" -- " + str(row[1]) + " views.")
    print()
    print()
    """ Second query """
    print("2. Who are the most popular article authors of all time?")
    print()

    second_cursor.execute("SELECT authors.name, COUNT(*) FROM articles JOIN log ON log.path = CONCAT('/article/', articles.slug) JOIN authors ON authors.id = articles.author WHERE log.status = '200 OK' GROUP BY authors.name ORDER BY COUNT(*) DESC;")
    result2 = second_cursor.fetchall()

    print()
    print("Answer: ")
    print()
    for row in result2:
        print("- " + row[0] + " -- " + str(row[1]) + " views.")
    print()
    print()

    """ Third query """
    """note: third query sometimes gives me end of transaction block error but closing the connection to
		DB and connecting to it again seems to make it magically works."""
    print("3. On which days did more than 1% of requests lead to errors?")
    print()

    third_cursor.execute("""SELECT t1.day, (TRUNC(CAST(t2.count::FLOAT / t1.count * 100 AS numeric),2)) AS "% error" FROM (SELECT TO_CHAR(time, 'FMMonth DD, YYYY') AS day, COUNT(*) FROM log GROUP BY day) AS t1 JOIN (SELECT TO_CHAR(time, 'FMMonth DD, YYYY') AS day, COUNT(*) FROM log WHERE status != '200 OK' GROUP BY day ORDER BY day) AS t2 ON t1.day = t2.day ORDER BY "% error" DESC LIMIT 1;""")
    result3 = third_cursor.fetchall()

    print()
    print("Answer: ")
    print()
    for row in result3:
        print("- " + row[0] + " -- " + str(row[1]) + "% errors.")
    print()
    print()


"""SELECT articles.title, COUNT(*) FROM articles JOIN log ON log.path = CONCAT('/article/', articles.slug) WHERE log.status = '200 OK' GROUP BY articles.title ORDER BY COUNT(*) DESC LIMIT 3;
SELECT authors.name, COUNT(*) FROM articles JOIN log ON log.path = CONCAT('/article/', articles.slug) JOIN authors ON authors.id = articles.author WHERE log.status = '200 OK' GROUP BY authors.name ORDER BY COUNT(*) DESC;
SELECT t1.day, (TRUNC(CAST(t2.count::FLOAT / t1.count * 100 AS numeric),2)) AS "% error" FROM (SELECT TO_CHAR(time, 'FMMonth DD, YYYY') AS day, COUNT(*) FROM log GROUP BY day) AS t1 JOIN (SELECT TO_CHAR(time, 'FMMonth DD, YYYY') AS day, COUNT(*) FROM log WHERE status != '200 OK' GROUP BY day ORDER BY day) AS t2 ON t1.day = t2.day ORDER BY "% error" DESC LIMIT 1;"""

if __name__ == '__main__':
    main()
