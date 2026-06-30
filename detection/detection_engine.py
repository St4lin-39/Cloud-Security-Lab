from detection.brute_force import detect_brute_force
from detection.resource_enumeration import detect_resource_enumeration
from detection.credential_stuffing import detect_credential_stuffing
from sqlalchemy.orm import Session

def run_detection_engine(db : Session, event):
    alerts = []
    brute_force = detect_brute_force(
        db=db,
        username = event.username,
        source_ip = event.ip_address
    )
    resource_enumeration = detect_resource_enumeration(
        db = db,
        username = event.username,
        source_ip = event.ip_address
    )
    credential_stuffing = detect_credential_stuffing(
        db = db,
        source_ip = event.ip_address
    )
    if brute_force:
        alerts.append(brute_force)

    if resource_enumeration:
        alerts.append(resource_enumeration)
        
    if credential_stuffing:
        alerts.append(credential_stuffing)
    
    return alerts

