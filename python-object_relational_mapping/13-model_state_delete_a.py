#!/usr/bin/python3
""" Deletes all State objects with a name containing the letter a """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    conn_string = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, db_name)

    engine = create_engine(conn_string)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_a = session.query(State).filter(State.name.contains('a')).all()

    for state in states_with_a:
        session.delete(state)

    session.commit()
    session.close()
