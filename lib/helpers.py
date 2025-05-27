from models import Agent, Client, House, AgentClient
from debug import session

# Agen t 
def add_agent(name):
    agent = Agent(agent_name=name)
    session.add(agent)
    session.commit()
    print(f"Agent '{name}' added.")

def list_agents():
    agents = session.query(Agent).all()
    for agent in agents:
        print(f"{agent.id}: {agent.agent_name}")

def delete_agent(agent_id):
    agent = session.get(Agent, agent_id)
    if agent:
        session.delete(agent)
        session.commit()
        print("Agent deleted.")
    else:
        print("Agent not found.")

# Clients
def add_client(name, phone, email):
    client = Client(client_name=name, phone_number=phone, email=email)
    session.add(client)
    session.commit()
    print(f"Client '{name}' added.")

def list_clients():
    clients = session.query(Client).all()
    for client in clients:
        print(f"{client.id}: {client.client_name} ({client.email})")

# Houses
def add_house(location, rooms, amount):
    house = House(location=location, no_of_rooms=rooms, amount=amount)
    session.add(house)
    session.commit()
    print(f"House in '{location}' added.")

def list_houses():
    houses = session.query(House).all()
    for house in houses:
        print(f"{house.id}: {house.location} - {house.no_of_rooms} rooms - Ksh {house.amount}")

# Assignments
def assign(agent_id, client_id, house_id):
    assignment = AgentClient(agent_id = agent_id, client_id = client_id, house_id = house_id)
    session.add(assignment)
    session.commit()
    print("Agent assigned to client for house.")