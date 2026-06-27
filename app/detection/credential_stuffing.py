from repositories.event_repository import get_unique_usernames_by_ip
from models.alert_model import AlertModel
from sqlalchemy.orm import Session
from datetime import datetime
from config.detection_rules import CREDENTIAL_STUFFING_THRESHOLD

def detect_credential_stuffing(db : Session, source_ip : str):
    usernames= get_unique_usernames_by_ip (db, source_ip)
    username_count= len(usernames)
    if username_count >= CREDENTIAL_STUFFING_THRESHOLD:
        return AlertModel(
            alert_type = "CREDENTIAL_STUFFING",
            username = "MULTIPLE_USERS",    
            source_ip = source_ip,
            attempts_volume = username_count,
            created_at = datetime.utcnow()
        )
    return None