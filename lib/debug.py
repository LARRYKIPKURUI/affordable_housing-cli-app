
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Agent, Client, House, Base  

# Create engine and session
engine = create_engine('sqlite:///my_database.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Create tables if they don't exist
Base.metadata.create_all(engine)

    