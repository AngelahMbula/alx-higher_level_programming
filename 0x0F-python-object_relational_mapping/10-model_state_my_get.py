#!/usr/bin/python3
"""Script that prints the State object with name passed as argument."""
if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(name=sys.argv[4]).first()
    if state is not None:
        print("{}".format(state.id))
    else:
        print("Not found")
