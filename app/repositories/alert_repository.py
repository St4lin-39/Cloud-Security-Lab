from sqlalchemy.orm import Session
from entities.alert_entity import AlertTable
from models.alert_model import AlertModel

def save_alert( db : Session, alert_model: AlertModel):
    try:
        alert = AlertTable(
            alert_type = alert_model.alert_type,
            username = alert_model.username,
            source_ip = alert_model.source_ip,
            attempts_volume = alert_model.attempts_volume,
            created_at = alert_model.created_at
        )
        db.add(alert)
        db.commit()
        db.refresh(alert)
        return alert
    except Exception: 
        db.rollback()
        raise