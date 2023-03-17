#!/usr/bin/python3
""" Table Print """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Connect to the database
    db_user, db_pass, db_name, db_host = sys.argv[1], sys.argv[2],
    sys.argv[3], "localhost"
    engine = create_engine(f"mysql+mysqldb://
    {db_user}:{db_pass}@{db_host}/{db_name}")
    Base.metadata.create_all(engine)

    # Query the database for the state with the given name
    with sessionmaker(bind=engine)() as session:
        state = session.query(State).filter(State.name == sys.argv[4]).first()

        # Print the ID of the state or "Not found" if no state is found
        if state is not None:
            print(state.id)
        else:
            print("Not found")
