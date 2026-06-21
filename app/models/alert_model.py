from pydantic import BaseModel
from datetime import datetime

class AlertModel(BaseModel):
    alert_type : str
    username : str
    source_ip : str
    attempts_volume : int
    created_at : datetime
