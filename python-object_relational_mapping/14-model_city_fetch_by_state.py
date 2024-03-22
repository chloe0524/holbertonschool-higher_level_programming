#!/usr/bin/python3
"""prints all cities from the database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    bdd_session = Session()

    for city, state in (bdd_session.query(City, State)
                        .join(State, City.state_id == State.id)
                        .order_by(City.id)):
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    bdd_session.commit()
    bdd_session.close()
