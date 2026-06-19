from datetime import datetime 
from models.alert_model import AlertModel
from repositories.alert_repository import save_alert

def generate_alert(db, 
                   alert_type: str,
                   username:str,
                   source_ip:str,
                   attempts_volume: int
                   ):
    alert_model = AlertModel(
        alert_type = alert_type,
        username = username,
        source_ip = source_ip,
        attempts_volume = attempts_volume,
        created_at = datetime.utcnow()
    )
    saved_alert = save_alert(
        alert_model= alert_model, db = db
    )
    return saved_alert

