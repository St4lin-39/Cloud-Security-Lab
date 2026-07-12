from repositories.event_repository import get_unique_usernames_by_ip
from models.alert_model import AlertModel
from sqlalchemy.orm import Session
from datetime import datetime
from config.detection_rules import CREDENTIAL_STUFFING_THRESHOLD
from models.event_model import EventModel
from repositories.alert_repository import has_recent_alert
from services.alert_factory import create_alert

def detect_credential_stuffing(db : Session, event : EventModel):
    already_alerted = has_recent_alert(
        db = db,
        alert_type = "CREDENTIAL_STUFFING",
        source_ip= event.ip_address
    )

    usernames= get_unique_usernames_by_ip(db, event.ip_address)
    username_count= len(usernames)
    if (username_count >= CREDENTIAL_STUFFING_THRESHOLD and not already_alerted):
        
        return create_alert(
            alert_type = "CREDENTIAL_STUFFING",
            username = None, 
            source_ip= event.ip_address,   
            attempts_volume = username_count
        )
    return None