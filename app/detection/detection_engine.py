from detection.brute_force import detect_brute_force
from detection.resource_enumeration import detect_resource_enumeration
from sqlalchemy import Session


def run_detection_engine(db: Session, event):
    alerts = []
    brute_force = detect_brute_force(
        db=db,
        username = event.username,
        source_ip = event.source_ip
    )
    if brute_force:
        alerts.append(brute_force)
        return alerts
    else:
        None
        
    resource_enumeration = detect_resource_enumeration(
        db = db,
        username = event.username,
        source_ip = event.source_ip
    )
    if resource_enumeration:
        alerts.append(resource_enumeration)
        return alerts
    else:
        None

