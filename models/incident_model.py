from pydantic import BaseModel
from datetime import datetime
class IncidentModel(BaseModel):
    incident_type : str
    classification : str
    classification_score : int
    severity : str
    priority : str
    status : str
    risk_score : int
    asset_criticality : str
    asset_criticality_score : int
    source_ip : str 
    alerts_count : int
    first_seen : datetime
    last_seen : datetime

