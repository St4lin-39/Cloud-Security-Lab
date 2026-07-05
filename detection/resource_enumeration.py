from datetime import datetime 
from models.alert_model import AlertModel
from sqlalchemy.orm import Session
from repositories.event_repository import get_unique_resources_by_username
from config.detection_rules import RESOURCE_ENUMERATION_THRESHOLD
from models.event_model import EventModel

def detect_resource_enumeration(db: Session, event : EventModel):
    resources = get_unique_resources_by_username(db, event.username)
    resource_count = len(resources)
    if resource_count >= RESOURCE_ENUMERATION_THRESHOLD:
        return AlertModel(
            alert_type = "RESOURCE_ENUMERATION",
            username = event.username,
            source_ip = event.source_ip,
            attempts_volume = resource_count,
            created_at = datetime.utcnow()

        )
    else:
        return None

