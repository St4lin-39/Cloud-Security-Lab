from pydantic import BaseModel
from datetime import datetime

class IncidentTimelineModel(BaseModel):
    incident_id : int
    event_type : str
    description : str
    created_at : datetime