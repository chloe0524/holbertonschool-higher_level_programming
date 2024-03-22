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

    bdd_session.add(State(name="Louisiana"))
    bdd_session.commit()
    louisiana = bdd_session.query(State).
    filter(State.name == "Louisiana").first()
    print(louisiana.id)
