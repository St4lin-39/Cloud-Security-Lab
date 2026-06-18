from pydantic import BaseModel
import datetime

class Alerts(BaseModel):
    id : int
    alert_type : str
    attempts_volume : int
    created_at : datetime
