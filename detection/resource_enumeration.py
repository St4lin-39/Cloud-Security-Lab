from datetime import datetime 
from models.alert_model import AlertModel
from sqlalchemy.orm import Session
from repositories.event_repository import get_unique_resources_by_username
from config.detection_rules import RESOURCE_ENUMERATION_THRESHOLD
from models.event_model import EventModel
from repositories.alert_repository import has_recent_alert
from config.alert_metadata import ALERT_METADATA

def detect_resource_enumeration(db: Session, event : EventModel):
    already_alerted= has_recent_alert(
        db = db,
        alert_type = "RESOURCE_ENUMERATION",
        source_ip= event.ip_address,
        username = event.username
    )
    metadata = ALERT_METADATA["RESOURCE_ENUMERATION"]
    resources = get_unique_resources_by_username(db, event.username)
    resource_count = len(resources)
    if (resource_count >= RESOURCE_ENUMERATION_THRESHOLD and not already_alerted):
        return AlertModel(
            alert_type = "RESOURCE_ENUMERATION",
            username = event.username,
            severity = metadata["severity"],
            status = "OPEN",
            description = metadata["description"],
            recommendation = metadata["recommendation"],
            source_ip = event.ip_address,
            attempts_volume = resource_count,
            created_at = datetime.utcnow()

        )
    else:
        return None

