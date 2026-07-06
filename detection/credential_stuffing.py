from repositories.event_repository import (
    get_unique_usernames_by_ip,
    get_unique_passwords_by_ip
)

from models.alert_model import AlertModel
from sqlalchemy.orm import Session
from models.event_model import EventModel
from datetime import datetime
from config.detection_rules import CREDENTIAL_STUFFING_THRESHOLD


def detect_credential_stuffing(db: Session, event: EventModel):

    usernames = get_unique_usernames_by_ip(
        db,
        event.ip_address
    )

    passwords = get_unique_passwords_by_ip(
        db,
        event.ip_address
    )

    username_count = len(usernames)
    password_count = len(passwords)

    if (
        username_count >= CREDENTIAL_STUFFING_THRESHOLD
        and
        password_count >= CREDENTIAL_STUFFING_THRESHOLD
    ):
        return AlertModel(
            alert_type="CREDENTIAL_STUFFING",
            username=None,
            source_ip=event.ip_address,
            attempts_volume=username_count,
            created_at=datetime.utcnow()
        )

    return None