from sqlalchemy import String, Integer, Column, DateTime
from database.connection import Base

class EventTable(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key= True, index= True)
    username = Column(String, nullable = False)
    ip_address = Column(String, nullable = False)
    event_type = Column(String, nullable = False)
    resource = Column(String, nullable = False)
    event_timestamp= Column(DateTime, nullable= False)