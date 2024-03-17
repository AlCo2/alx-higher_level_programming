#!/usr/bin/python3
""" connect to database and fetch some data """
import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]
    db = MySQLdb.connect(host="localhost",
                         user=username, passwd=password, db=database)
    cur = db.cursor()
    cur.execute("""SELECT cities.name
                FROM cities INNER JOIN
                states ON cities.state_id = states.id
                where states.name LIKE BINARY %s
                ORDER BY cities.id""", (state,))
    rows = cur.fetchall()
    for i, row in enumerate(rows):
        print(row[0], end='')
        if i <= len(row):
            print(', ', end='')
    cur.close()
    db.close()
