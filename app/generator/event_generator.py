from datetime import datetime
from models.event_model import EventModel
from repositories.event_repository import save_event

def generate_event(db, 
                   username:str,
                   ip_address:str,
                   event_type: str,
                   resource:str):
    event_model = EventModel(
        username = username,
        ip_address = ip_address,
        event_type = event_type,
        resource = resource,
        event_timestamp = datetime.utcnow()
    )
    if not username:
        raise("El usuario no deberia estar vacio")
    
    saved_event = save_event(
        db = db, event_model = event_model
    )
    return saved_event