#!/usr/bin/python3
"""module deleting all State with name containing 'a'"""

from sqlalchemy import create_engine, insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    bdd_session = Session()
    bdd_session.query(State).filter(State.name.like('%a%')).delete()
    bdd_session.commit()
    bdd_session.close()
