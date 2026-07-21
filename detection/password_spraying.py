from repositories.event_repository import count_unique_users_by_password_attempt
from config.detection_rules import PASSWORD_SPRAYING_THRESHOLD
from models.event_model import EventModel
from sqlalchemy.orm import Session 
from repositories.alert_repository import has_recent_alert
from services.alert_factory import create_alert

def detect_password_spraying(db : Session, event : EventModel):
    already_alerted = has_recent_alert(
        db = db,
        alert_type = "PASSWORD_SPRAYING",
        source_ip= event.ip_address
    )
    
    password_attempts = count_unique_users_by_password_attempt(db, event.password_attempt)
    user_count= len(password_attempts)
    if (user_count >= PASSWORD_SPRAYING_THRESHOLD and not already_alerted):
        
        return create_alert(
            alert_type = "PASSWORD_SPRAYING",
            username = None,
            source_ip = event.ip_address,
            resource = event.resource,
            attempts_volume = user_count,
        )
    return None