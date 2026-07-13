from sqlalchemy import String, Integer, Column, DateTime, Text
from database.connection import Base

class AlertTable(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key = True, index= True)
    username = Column(String, nullable = True)
    source_ip = Column(String, nullable = False)
    alert_type = Column(String, nullable = False)
    severity = Column(String, nullable = False)
    risk_score = Column(Integer, nullable = False)
    confidence = Column(Integer, nullable = False)
    status = Column(String, nullable = False)
    description = Column(Text, nullable = False)
    recommendation = Column(Text, nullable = False)
    mitre_tactic = Column(String, nullable = True)
    mitre_technique = Column(String, nullable = True)
    attempts_volume = Column(Integer, nullable = False)
    created_at = Column(DateTime, nullable = False)