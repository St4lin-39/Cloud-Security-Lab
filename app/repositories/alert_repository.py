from sqlalchemy.orm import Session
from entities.alert_entity import AlertTable
from models.alert_model import AlertModel
from datetime import datetime, timedelta
from config.detection_rules import ALERT_COOLDOWN_MINUTES, CORRELATION_INTERVAL_MINUTES
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

def has_recent_alert(db : Session, alert_type : str, source_ip : str):
    start_time = datetime.utcnow() - timedelta(minutes = ALERT_COOLDOWN_MINUTES)
    recent_alert = db.query(AlertTable).filter(AlertTable.alert_type == alert_type).filter(AlertTable.source_ip == source_ip).filter(AlertTable.created_at >= start_time).first()
    if recent_alert:
        return True
    else:
        return False

def get_recent_alerts_by_ip(db : Session, source_ip : str):
    start_time = datetime.utcnow() - timedelta(minutes = CORRELATION_INTERVAL_MINUTES)
    return( db.query(AlertTable).filter(AlertTable.source_ip == source_ip).filter(AlertTable.created_at >= start_time).all())