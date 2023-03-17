#!/usr/bin/python3
""" Delete States with 'a' """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states_with_a():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    with sessionmaker(bind=engine)() as session:
        num_deleted = session.query(State).filter(State.name.like('%a%')).delete()
        session.commit()
        print(f"Deleted {num_deleted} states with 'a' in their name")


if __name__ == "__main__":
    delete_states_with_a()
