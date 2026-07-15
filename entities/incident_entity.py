from sqlalchemy import String, Integer, Column, DateTime
from database.connection import Base


class IncidentTable(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key= True, index= True)
    incident_type = Column(String, nullable = False)
    severity = Column(String, nullable = False)
    priority = Column(String, nullable = False)
    status = Column(String, nullable = False)
    risk_score = Column(Integer, nullable = False)
    source_ip = Column(String, nullable = False)
    alerts_count = Column(Integer, nullable = False)
    first_seen = Column(DateTime, nullable = False)
    last_seen = Column(DateTime, nullable = False)
