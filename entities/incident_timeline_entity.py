from sqlalchemy import String, Integer, Column, ForeignKey, DateTime
from database.connection import Base

class IncidentTimelineTable(Base):
    __tablename__ = "incident_timeline"
    id = Column(Integer, primary_key= True, index = True)
    incident_id= Column(Integer, ForeignKey("incidents.id"), nullable = False)
    event_type = Column(String, nullable = False)
    description = Column(String, nullable = False)
    created_at = Column(DateTime, nullable = False)
