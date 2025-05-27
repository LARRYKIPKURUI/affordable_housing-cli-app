from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

# Agents Table
class Agent(Base):
    __tablename__ = 'agents'

    id = Column(Integer, primary_key=True)
    agent_name = Column(String)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    assignments = relationship("AgentClient", back_populates="agent")

    def __repr__(self):
        return f'<Agent {self.agent_name}>'

# Clients Table
class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    client_name = Column(String)
    phone_number = Column(String)
    email = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    assignments = relationship("AgentClient", back_populates="client")

    def __repr__(self):
        return f'<Client {self.client_name}>'

# Houses Table
class House(Base):
    __tablename__ = 'houses'

    id = Column(Integer, primary_key=True)
    location = Column(String)
    amount = Column(Integer)
    no_of_rooms = Column(Integer)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    assignments = relationship("AgentClient", back_populates="house")

    def __repr__(self):
        return f'<House {self.id} has {self.no_of_rooms} rooms and is located at {self.location}>'

# Junction Table (Agent assigned to Client for a specific House)
class AgentClient(Base):
    __tablename__ = 'agents_clients'

    id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, ForeignKey('agents.id'))
    client_id = Column(Integer, ForeignKey('clients.id'))
    house_id = Column(Integer, ForeignKey('houses.id'))
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    agent = relationship("Agent", back_populates="assignments")
    client = relationship("Client", back_populates="assignments")
    house = relationship("House", back_populates="assignments")
