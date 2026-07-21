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
            severity = alert_model.severity,
            confidence = alert_model.confidence,
            risk_score = alert_model.risk_score,
            asset_criticality = alert_model.asset_criticality,
            asset_criticality_score = alert_model.asset_criticality_score,
            status = alert_model.status,
            description = alert_model.description,
            recommendation = alert_model.recommendation,
            mitre_tactic = alert_model.mitre_tactic,
            mitre_technique = alert_model.mitre_technique,
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

def has_recent_alert(db : Session, alert_type : str, source_ip : str, username : str | None=None):
    start_time = datetime.utcnow() - timedelta(minutes = ALERT_COOLDOWN_MINUTES)
    query = (db.query(AlertTable).filter(AlertTable.alert_type == alert_type).filter(AlertTable.source_ip == source_ip).filter(AlertTable.created_at >= start_time))
    if username is not None:
        query = query.filter(AlertTable.username == username)
    
    return query.first() is not None

def get_recent_alerts_by_ip(db : Session, source_ip : str):
    start_time = datetime.utcnow() - timedelta(minutes = CORRELATION_INTERVAL_MINUTES)
    return( db.query(AlertTable).filter(AlertTable.source_ip == source_ip).filter(AlertTable.created_at >= start_time).all())