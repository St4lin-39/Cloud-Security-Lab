from models.alert_model import AlertModel
from sqlalchemy.orm import Session
from repositories.event_repository import count_failed_logins_by_username
from datetime import datetime 
from config.detection_rules import BRUTE_FORCE_INTERVAL_THRESHOLD

def detect_brute_force(db: Session, username : str, source_ip : str):
    failed_attempts = count_failed_logins_by_username(db, username)
    print(f"Usuario = {username} Intentos={failed_attempts}")
    if failed_attempts >= BRUTE_FORCE_INTERVAL_THRESHOLD:
        return AlertModel(
            alert_type = "BRUTE_FORCE_ATTEMPT",
            username = username,
            source_ip = source_ip,
            attempts_volume = failed_attempts,
            created_at = datetime.utcnow()
        )
    
    else:
        return None