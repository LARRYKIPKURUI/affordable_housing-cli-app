from models import Agent, Client, House, AgentClient
from sqlalchemy.exc import SQLAlchemyError #using sqlalchemy .excemption to handle errors in try catch blocks

# AGENTS
def add_agent(session, name):
    try:
        existing = session.query(Agent).filter_by(agent_name=name).first()
        if existing:
            print(f"Agent '{name}' already exists.")
            return
        agent = Agent(agent_name=name)
        session.add(agent)
        session.commit()
        print(f"Agent '{name}' added.")
    except SQLAlchemyError as e:
        session.rollback() #using rollback to avoid keeping session in error state
        print(f"Error adding agent: {e}")

def list_agents(session):
    agents = session.query(Agent).all()
    for agent in agents:
        print(f"{agent.id}: {agent.agent_name}")

def delete_agent(session, agent_id):
    try:
        agent = session.get(Agent, agent_id)
        if agent:
            session.delete(agent)
            session.commit()
            print("Agent deleted.")
        else:
            print("Agent not found.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error deleting agent: {e}")

# CLIENTS
def add_client(session, name, phone, email):
    try:
        existing = session.query(Client).filter_by(email=email).first()
        if existing:
            print(f"Client with email '{email}' already exists.")
            return
        client = Client(client_name=name, phone_number=phone, email=email)
        session.add(client)
        session.commit()
        print(f"Client '{name}' added.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error adding client: {e}")

def list_clients(session):
    clients = session.query(Client).all()
    for client in clients:
        print(f"{client.id}: {client.client_name} ({client.email})")

def delete_client(session, client_id):
    try:
        client = session.get(Client, client_id)
        if client:
            session.delete(client)
            session.commit()
            print("Client deleted.")
        else:
            print("Client not found.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error deleting agent: {e}")

# HOUSES
def add_house(session, location, rooms, amount):
    try:
        house = House(location=location, no_of_rooms=rooms, amount=amount)
        session.add(house)
        session.commit()
        print(f"House in '{location}' added.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error adding house: {e}")

def list_houses(session):
    houses = session.query(House).all()
    for house in houses:
        print(f"{house.id}: {house.location} - {house.no_of_rooms} rooms - Ksh {house.amount}")

# ASSIGNMENTS
def assign(session, agent_id, client_id, house_id):
    try:
        # Check if assignment already exists (basically if already assigned)
        existing = session.query(AgentClient).filter_by(
            agent_id=agent_id,
            client_id=client_id,
            house_id=house_id
        ).first()

        if existing:
            print("This assignment already exists.")
            return

        assignment = AgentClient(agent_id=agent_id, client_id=client_id, house_id=house_id)
        session.add(assignment)
        session.commit()
        print("Agent assigned to client for house.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error assigning agent: {e}")
