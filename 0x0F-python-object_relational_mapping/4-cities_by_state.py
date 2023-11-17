#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    # check number of arguments
    if len(sys.argv) != 4:
        print(
            "Usage: {} <username> <password> <database> <state_name>".format(
                sys.argv[0]
            )
        )
        sys.exit(1)

    # connect to database
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
    )
    cur = db.cursor()

    # create query and run query
    query = "SELECT cities.id, cities.name, states.name FROM states RIGHT JOIN cities ON states.id = cities.state_id ORDER BY cities.id"
    cur.execute(query)

    # fetch and print results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # clean up
    cur.close()
    db.close()
