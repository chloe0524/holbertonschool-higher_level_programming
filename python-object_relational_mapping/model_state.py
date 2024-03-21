#!/usr/bin/python3
"""class definition of a state"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    bdd = sys.argv[3]
    engine = create_engine(f'mysql+mysqldb://{user}:{password}@localhost/{db}',
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
