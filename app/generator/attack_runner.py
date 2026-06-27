from sqlalchemy.orm import Session

from generator.event_generator import generate_event
from detection.detection_engine import run_detection_engine
from services.alert_manager import process_alert

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

        alerts = run_detection_engine(
            db = db, event = event
        )
        for alert in alerts:
            saved_alert = process_alert(
                db = db, alert_model = alert
            )
            if saved_alert:
                generated_alerts.append(saved_alert)
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

        alerts = run_detection_engine(
            db = db,
            event = event
        )
        for alert in alerts:
            saved_alert = process_alert(
                db = db,
                alert_model = alert
            )
            if saved_alert:
                generated_alerts.append(saved_alert)
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
        alerts = run_detection_engine(
            db = db,
            event = event
        )
        for alert in alerts:
            saved_alerts = process_alert(
                db = db,
                alert_model = alert
            )
            if saved_alerts:
                generated_alerts.append(saved_alerts)
    return generated_events, generated_alerts

