from sqlalchemy.orm import Session

from generator.event_generator import generate_event
from detection.detection_engine import run_detection_engine
from repositories.alert_repository import save_alert

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
            saved_alert = save_alert(
                db = db, alert_model = alert
            )
            generated_alerts.append(saved_alert)
    return generated_events, generated_alerts  