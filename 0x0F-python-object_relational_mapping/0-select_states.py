#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Database connection parameters
    host = "localhost"
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    port = 3306

    db = MySQLdb.connect(host=host, user=user, passwd=password, db=database, port=port)

    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
