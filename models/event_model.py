from pydantic import BaseModel
from datetime import datetime
class EventModel(BaseModel):
    username : str
    ip_address : str
    event_type : str
    resource : str
    event_timestamp: datetime