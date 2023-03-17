#!/usr/bin/python3
""" Update State Name """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def update_state_name_in_database():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    with sessionmaker(bind=engine)() as session:
        state_to_update = session.query(State).filter(State.id == 2).first()
        state_to_update.name = 'New Mexico'
        session.commit()
        print(f"State name updated: {state_to_update}")


if __name__ == "__main__":
    update_state_name_in_database()
