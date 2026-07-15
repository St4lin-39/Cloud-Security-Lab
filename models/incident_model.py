from pydantic import BaseModel
from datetime import datetime
class IncidentModel(BaseModel):
    incident_type : str
    severity : str
    priority : str
    status : str
    risk_score : int
    source_ip : str 
    alerts_count : int
    first_seen : datetime
    last_seen : datetime

