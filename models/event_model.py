from pydantic import BaseModel
from datetime import datetime
from typing import Optional
class EventModel(BaseModel):
    username : str
    ip_address : str
    event_type : str
    resource : str
    password_attempt : Optional[str] = None
    event_timestamp: datetime
    