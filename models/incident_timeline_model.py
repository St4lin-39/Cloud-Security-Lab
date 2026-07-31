from pydantic import BaseModel
from datetime import datetime

class IncidentTimelineModel(BaseModel):
    incident_id : str
    event_type : str
    description : str
    created_at : datetime