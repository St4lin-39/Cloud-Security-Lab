from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AlertModel(BaseModel):
    alert_type : str
    username : Optional[str] = None
    source_ip : str
    attempts_volume : int
    created_at : datetime
