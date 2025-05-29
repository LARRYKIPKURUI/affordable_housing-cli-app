from models import Agent, Client, House, AgentClient
from debug import Session, init_db

# Ensure tables are created
init_db()

with Session() as session:
    # Create agents
    agent1 = Agent(agent_name="Alice")
    agent2 = Agent(agent_name="Bob")

    # Create clients
    client1 = Client(client_name="Charlie", phone_number="0712345678", email="charlie@example.com")
    client2 = Client(client_name="Diana", phone_number="0798765432", email="diana@example.com")

    # Create houses
    house1 = House(location="Kilimani", no_of_rooms=3, amount=85000)
    house2 = House(location="Westlands", no_of_rooms=2, amount=65000)

    # Create assignments
    assignment1 = AgentClient(agent=agent1, client=client1, house=house1)
    assignment2 = AgentClient(agent=agent2, client=client2, house=house2)

    # Seed all at once
    session.add_all([agent1, agent2, client1, client2, house1, house2, assignment1, assignment2])
    session.commit()

print("Seeded my_database successfully!")

