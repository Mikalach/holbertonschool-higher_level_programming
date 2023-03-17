#!/usr/bin/python3
""" Add State """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def add_state_to_database():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print(f"Added new state with id {new_state.id}")

    session.close()


if __name__ == "__main__":
    add_state_to_database()
