#!/usr/bin/python3
"""module printing  first State from database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    bdd_session = Session()

    for state in bdd_session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

    if state:
        print("{}: {}".format(state.id, state.name))
    print('Nothing')
    bdd_session.close()
