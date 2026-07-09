from models.alert_model import AlertModel
from sqlalchemy.orm import Session
from repositories.event_repository import count_failed_logins_by_username
from datetime import datetime 
from config.detection_rules import BRUTE_FORCE_THRESHOLD
from models.event_model import EventModel
from repositories.alert_repository import has_recent_alert
from config.alert_metadata import ALERT_METADATA

def detect_brute_force(db: Session, event : EventModel):
    already_alerted = has_recent_alert(
        db = db,
        alert_type = "BRUTE_FORCE",
        source_ip= event.ip_address,
        username = event.username
    )
    metadata = ALERT_METADATA["BRUTE_FORCE_ATTEMPT"]
    failed_attempts = count_failed_logins_by_username(db, event.username)
    print(f"Usuario = {event.username} Intentos={failed_attempts}")
    if (failed_attempts >= BRUTE_FORCE_THRESHOLD and not already_alerted):
        
        return AlertModel(
            alert_type = "BRUTE_FORCE_ATTEMPT",
            severity = metadata["severity"],
            status = "OPEN",
            description = metadata["description"],
            recommendation = metadata["recommendation"],
            username = event.username,
            source_ip = event.ip_address,
            attempts_volume = failed_attempts,
            created_at = datetime.utcnow()
        )
    return None