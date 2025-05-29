from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base  

# Create engine
engine = create_engine('sqlite:///my_database.db', echo=True)

# Creating a configured "Session" class
Session = sessionmaker(bind=engine)

# Function to initialize DB schema,,(
def init_db():
    Base.metadata.create_all(engine)
