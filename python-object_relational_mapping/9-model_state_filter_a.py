#!/usr/bin/python3
""" lists all State objects that contain the letter a from the database """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        query = session.query(State.id, State.name).filter(State.name.contains
                                                           ('a'))
        for row in query:
            print(f"{row[0]}: {row[1]}")
