from sqlalchemy import String, Integer, Column, DateTime
from database.connection import Base

class AlertTable(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key = True, index= True)
    source_ip = Column(String, nullable = False)
    alert_type = Column(String, nullable = False)
    attempts_volume = Column(Integer, nullable = False)
    created_at = Column(DateTime, nullable = False)