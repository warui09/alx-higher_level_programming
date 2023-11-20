#!/usr/bin/python3
"""
Prints the State object with the name passed as argument from the database
hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
import sys

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Create a connection to the database
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )

    # Create a session
    session = Session(engine)

    # Query the State object with the specified name
    state_name_to_search = sys.argv[4]
    query = text("SELECT * FROM states WHERE name = :name")
    state = session.execute(query, {"name": state_name_to_search}).fetchone()

    if state:
        print(state.id)
    else:
        print("Not found")


    # Close the session
    session.close()
