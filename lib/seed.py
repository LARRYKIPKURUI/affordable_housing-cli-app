from models import Agent, Client, House, AgentClient, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timezone

engine = create_engine('sqlite:///my_database.db')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)  # Ensure all tables are created

# Add agents
agent1 = Agent(agent_name="Alice")
agent2 = Agent(agent_name="Bob")

# Add clients
client1 = Client(client_name="Charlie", phone_number="0712345678", email="charlie@example.com")
client2 = Client(client_name="Diana", phone_number="0798765432", email="diana@example.com")

# Add houses
house1 = House(location="Kilimani", no_of_rooms=3, amount=85000)
house2 = House(location="Westlands", no_of_rooms=2, amount=65000)

# Add assignments
assignment1 = AgentClient(agent=agent1, client=client1, house=house1)
assignment2 = AgentClient(agent=agent2, client=client2, house=house2)

session.add_all([agent1, agent2, client1, client2, house1, house2, assignment1, assignment2])
session.commit()

print("Seeded to my_database successfully!")
