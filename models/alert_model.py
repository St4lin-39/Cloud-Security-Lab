from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AlertModel(BaseModel):
    alert_type : str
    severity : str
    confidence: int
    risk_score: int
    status : str
    description : str
    recommendation : str
    mitre_tactic : Optional[str] = None
    mitre_technique : Optional[str] = None
    username : Optional[str] = None
    source_ip : str
    attempts_volume : int
    created_at : datetime
