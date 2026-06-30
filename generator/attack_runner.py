from sqlalchemy.orm import Session
from generator.event_generator import generate_event
from services.detection_pipeline import process_event

def run_brute_force_attack(db : Session, username : str, ip_address : str, attempts : int):
    generated_events = []
    generated_alerts = []

    for _ in range(attempts):
        event = generate_event(
            db = db,
            username = username,
            ip_address = ip_address,
            event_type = "LOGIN_FAILED",
            resource = "/login"
        )
        generated_events.append(event)

        alerts = process_event(
            db = db,
            event = event
        )
        generated_alerts.extend(alerts)
       
    return generated_events, generated_alerts  

def run_resource_enumeration_attack(db: Session, username : str, ip_address : str, resources : list[str]):
    generated_events = []
    generated_alerts = []
    for resource in resources:
        event = generate_event(
            db = db,
            username = username,
            ip_address = ip_address,
            event_type = "RESOURCE_ACCESS",
            resource = resource
        )
        generated_events.append(event)

        alerts = process_event(
            db = db,
            event = event
        )
        generated_alerts.extend(alerts)
    return generated_events, generated_alerts

def run_credential_stuffing_attack(db : Session, username : list[str], ip_address : str):
    generated_events = []
    generated_alerts = []

    for usernames in username:
        event = generate_event(
            db = db,
            username = usernames,
            ip_address = ip_address,
            event_type = "LOGIN_FAILED",
            resource = "/login"
        )
        generated_events.append(event)
        alerts = process_event(
            db = db,
            event = event
        )
        generated_alerts.extend(alerts)
    return generated_events, generated_alerts

