#!/usr/bin/python3
""" Module documented """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    with sessionmaker(bind=engine)() as session:
        query = session.query(State.id, State.name).first()
        if query:
            print(f"{query.id}: {query.name}")
        else:
            print("Nothing")
