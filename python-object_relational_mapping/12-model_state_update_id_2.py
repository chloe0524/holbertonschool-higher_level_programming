#!/usr/bin/python3
"""module changing/updating name of a state from the database """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    bdd_session = Session()

    session.query(State).filter(
        State.id == 2).update({'name': 'New Mexico'})
    session.commit()
    session.close()
