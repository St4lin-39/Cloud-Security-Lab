from sqlalchemy.orm import Session 
from repositories.alert_repository import get_recent_alerts_by_ip
from models.alert_model import AlertModel
from datetime import datetime 

def correlate_alerts(db : Session, source_ip: str):
    alerts = get_recent_alerts_by_ip(
        db = db,
        source_ip = source_ip
    )
    alert_types = set()

    for alert in alerts:
        alert_types.add(alert.alert_type)
    
    required_alerts ={
        "BRUTE_FORCE_ATTEMPT",
        "RESOURCE_ENUMERATION",
        "CREDENTIAL_STUFFING"
    } 
    if required_alerts.issubset(alert_types):
        return AlertModel(
            username = "MULTIPLE_USERS",
            source_ip = source_ip,
            alert_type = "MULTI_STAGE_ATTACK",
            attempts_volume = len(alerts),
            created_at= datetime.utcnow()
        )
    else:
        return None