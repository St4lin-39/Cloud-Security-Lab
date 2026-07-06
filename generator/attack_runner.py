from sqlalchemy.orm import Session
from generator.event_generator import generate_event
from services.detection_pipeline import process_event
from generator.simulation_data import get_random_brute_force_password, get_password_spraying_password
from generator.simulation_data import get_leaked_password
def run_brute_force_attack(db : Session, username : str, ip_address : str, attempts : int):
    generated_events = []
    generated_alerts = []

    for _ in range(attempts):
        event = generate_event(
            db = db,
            username = username,
            ip_address = ip_address,
            event_type = "LOGIN_FAILED",
            resource = "/login",
            password_attempt = get_random_brute_force_password()
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
            resource = resource,
            password_attempt = None
        )
        generated_events.append(event)

        alerts = process_event(
            db = db,
            event = event
        )
        generated_alerts.extend(alerts)
    return generated_events, generated_alerts

def run_credential_stuffing_attack(
    db: Session,
    usernames: list[str],
    ip_address: str
):

    generated_events = []
    generated_alerts = []

    for username in usernames:

        password = get_leaked_password(username)

        event = generate_event(
            db=db,
            username=username,
            ip_address=ip_address,
            event_type="LOGIN_FAILED",
            resource="/login",
            password_attempt=password
        )

        generated_events.append(event)

        alerts = process_event(
            db=db,
            event=event
        )

        generated_alerts.extend(alerts)

    return generated_events, generated_alerts

def run_password_spraying_attack(
    db: Session,
    usernames: list[str],
    ip_address: str,
    password_attempt: str
):

    generated_events = []
    generated_alerts = []

    for username in usernames:

        event = generate_event(
            db=db,
            username=username,
            ip_address=ip_address,
            event_type="LOGIN_FAILED",
            resource="/login",
            password_attempt=password_attempt
        )

        generated_events.append(event)

        alerts = process_event(
            db=db,
            event=event
        )

        generated_alerts.extend(alerts)

    return generated_events, generated_alerts
