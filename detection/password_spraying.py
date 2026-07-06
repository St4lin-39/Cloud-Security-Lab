from repositories.event_repository import count_unique_users_by_password_attempt
from config.detection_rules import PASSWORD_SPRAYING_THRESHOLD
from models.alert_model import AlertModel
from models.event_model import EventModel
from datetime import datetime
from sqlalchemy.orm import Session 


def detect_password_spraying(db : Session, event : EventModel):
    password_attempts = count_unique_users_by_password_attempt(db, event.password_attempt)
    user_count= len(password_attempts)
    if user_count >= PASSWORD_SPRAYING_THRESHOLD:
        return AlertModel(
            alert_type = "PASSWORD_SPRAYING",
            username = None,
            source_ip = event.ip_address,
            attempts_volume = user_count,
            created_at = datetime.utcnow()
        )
    return None