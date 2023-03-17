#!/usr/bin/python3
""" Module documentend """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    db_user, db_pass, db_name, db_host = sys.argv[1], sys.argv[2], \
        sys.argv[3], "localhost"
    engine = create_engine(f"mysql+mysqldb:
//{db_user}:{db_pass}@{db_host}/{db_name}")
    Base.metadata.create_all(engine)

    with sessionmaker(bind=engine)() as session:
        state = session.query(State).filter(State.name == sys.argv[4]).first()

        if state is not None:
            print(state.id)
        else:
            print("Not found")
