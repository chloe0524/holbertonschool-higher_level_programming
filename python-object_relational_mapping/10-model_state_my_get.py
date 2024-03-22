#!/usr/bin/python3
"""lists all State objects that contain the letter a"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    bdd_session = Session()

    state = bdd_session.query(State)\
        .filter(State.name == sys.argv[4])\
        .first()

    if state:
        print(state.id)
    else:
        print("Not found")

    bdd_session.close()
