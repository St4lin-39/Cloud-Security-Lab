
from sqlalchemy.orm import Session
from entities.event_entity import EventTable
from models.event_model import EventModel


def save_event(event_model: EventModel, db : Session):
    try:
        event = EventTable(
            username = event_model.username,
            ip_address = event_model.ip_address,
            event_type = event_model.event_type,
            resource = event_model.resource,
            event_timestamp = event_model.event_timestamp
        )
        db.add(event)
        db.commit()
        db.refresh(event)
        return event
    except Exception:
        db.rollback()
        raise 
