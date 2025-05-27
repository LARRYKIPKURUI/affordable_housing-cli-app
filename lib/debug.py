
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Agent,CLient,House

#Create Database Connection.
if __name__ == '__main__':
    
    engine = create_engine('sqlite:///my_database.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    