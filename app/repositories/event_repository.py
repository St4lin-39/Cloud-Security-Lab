from sqlalchemy.orm import Session
from entities.event_entity import EventTable
from models.event_model import EventModel
from datetime import datetime, timedelta
from config.detection_rules import BRUTE_FORCE_INTERVAL_MINUTES
from config.detection_rules import RESOURCE_ENUMERATION_INTERVAL_MINUTES
from config.detection_rules import CREDENTIAL_STUFFING_INTERVAL_MINUTES

def save_event(db : Session, event_model: EventModel):
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

def count_failed_logins_by_username(db: Session, username: str):
    return(
        db.query(EventTable).filter(EventTable.username == username).filter(EventTable.event_type == "LOGIN_FAILED").count()
    )

def get_unique_resources_by_username(db : Session, username: str):
       start_time = datetime.utcnow() - timedelta(minutes = RESOURCE_ENUMERATION_INTERVAL_MINUTES)
       resources =  db.query(EventTable.resource).filter(EventTable.username == username).filter(EventTable.event_type == "RESOURCE_ACCESS").filter(EventTable.event_timestamp >= start_time).distinct().all()
       return[
            row[0]
            for row in resources
       ]
    
def get_unique_usernames_by_ip(db: Session, ip_address : str):
     start_time = datetime.utcnow() - timedelta(minutes = CREDENTIAL_STUFFING_INTERVAL_MINUTES)
     usernames = db.query(EventTable.username).filter(EventTable.ip_address == ip_address).filter(EventTable.event_type == "LOGIN_FAILED").filter(EventTable.event_timestamp >= start_time ).distinct().all()
     return[
          row[0]
          for row in usernames
     ]

def count_failed_logins_by_username_since(db : Session, username : str):
     start_time = datetime.utcnow() - timedelta(minutes = BRUTE_FORCE_INTERVAL_MINUTES)
     return(
     db.query(EventTable).filter(EventTable.username == username).filter(EventTable.event_type == "LOGIN_FAILED").filter(EventTable.event_timestamp >= start_time).count()
     )

