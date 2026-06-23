from sqlalchemy.orm import Session
from entities.event_entity import EventTable
from models.event_model import EventModel


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
       resources =  db.query(EventTable.resource).filter(EventTable.username == username).distinct().all()
       return[
            row[0]
            for row in resources
       ]
    
def get_unique_usernames_by_ip(db: Session, ip_address : str):
     usernames = db.query(EventTable.username).filter(EventTable.ip_address == ip_address).filter(EventTable.event_type == "LOGIN_FAILED").distinct().all()
     return[
          row[0]
          for row in usernames
     ]