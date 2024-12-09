#!/usr/bin/python3
"""
Lists all State objects and corresponding City objects in the database hbtn_0e_101_usa.
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City
from sqlalchemy.orm import joinedload

if __name__ == "__main__":
    # Command-line arguments: username, password, database name
    username, password, db_name = argv[1], argv[2], argv[3]

    # Database connection setup
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query states and related cities, sorted by state.id and city.id
    states = session.query(State).options(joinedload(State.cities)).order_by(State.id).all()

    # Print results
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in sorted(state.cities, key=lambda x: x.id):
            print(f"    {city.id}: {city.name}")
    
    session.close()

