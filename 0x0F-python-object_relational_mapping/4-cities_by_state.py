#!/usr/bin/python3
""" connect to database and fetch some data """
import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host="localhost",
                         user=username, passwd=password, db=database)
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities INNER JOIN
                states ON cities.state_id = states.id
                ORDER BY cities.id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
