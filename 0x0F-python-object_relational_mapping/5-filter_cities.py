#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    # check number of arguments
    if len(sys.argv) != 5:
        print(
            "Usage: {} <username> <password> <database> <state_name> state".format(
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
    query = "SELECT cities.name FROM states RIGHT JOIN cities ON states.id = cities.state_id WHERE states.name=%s ORDER BY cities.id"
    cur.execute(query, (sys.argv[4],))

    # fetch and print results
    rows = cur.fetchall()
    for row in rows:
        print(row[0])

    # clean up
    cur.close()
    db.close()
