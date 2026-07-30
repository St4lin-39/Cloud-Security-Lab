from sqlalchemy import String, Integer, Column, DateTime
from database.connection import Base


class IncidentTable(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key= True, index= True)
    classification = Column(String, nullable = False)
    classification_score = Column(Integer, nullable = False)
    incident_type = Column(String, nullable = False)
    severity = Column(String, nullable = False)
    priority = Column(String, nullable = False)
    status = Column(String, nullable = False)
    risk_score = Column(Integer, nullable = False)
    asset_criticality = Column(String, nullable = False)
    asset_criticality_score = Column(Integer, nullable = False)
    source_ip = Column(String, nullable = False)
    alerts_count = Column(Integer, nullable = False)
    first_seen = Column(DateTime, nullable = False)
    last_seen = Column(DateTime, nullable = False)
