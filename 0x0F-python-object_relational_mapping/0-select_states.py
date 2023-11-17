#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""


def main():
    """
    Main function that will only be called when the script is run directly
    not imported
    """
    import MySQLdb
    import sys

    # Database connection parameters
    host = "localhost"
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    port = 3306

    db = MySQLdb.connect(host=host, user=user, passwd=password, db=database, port=port)

    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
