from datetime import datetime 
from models.alert_model import AlertModel
from sqlalchemy.orm import Session
from repositories.event_repository import count_failed_logins_by_username, get_unique_resources_by_username


def detect_brute_force(db: Session, username : str, source_ip : str):
    failed_attempts = count_failed_logins_by_username(db, username)
    if failed_attempts >= 5:
        return AlertModel(
            alert_type = "BRUTE_FORCE_ATTEMPT",
            username = username,
            source_ip = source_ip,
            attempts_volume = failed_attempts,
            created_at = datetime.utcnow()
        )
    else:
        return None

def detect_resource_enumeration(db: Session, username : str, source_ip : str):
    resources = get_unique_resources_by_username(db, username)
    resource_count = len(resources)
    if resource_count >= 10:
        return AlertModel(
            alert_type = "RESOURCE_ENUMERATION",
            username = username,
            source_ip = source_ip,
            attempts_volume = resource_count,
            created_at = datetime.utcnow()

        )
    else:
        return None