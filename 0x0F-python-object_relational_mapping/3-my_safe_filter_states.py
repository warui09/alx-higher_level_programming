#!/usr/bin/python3
"""
Takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    # check number of arguments
    if len(sys.argv) != 5:
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

    # set up query
    query = "SELECT * FROM states WHERE name=%s ORDER BY id"
    cur.execute(query, (sys.argv[4],))

    # fetch and print results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # clean up
    cur.close()
    db.close()
