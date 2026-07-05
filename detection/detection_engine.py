from sqlalchemy.orm import Session
from detection.detection_registry import DETECTORS

def run_detection_engine(db : Session, event):
    alerts = []
    for detector in DETECTORS:
        alert = detector(
            db = db,
            event = event
        )
        if alert:
            alerts.append(alert)
        
    return alerts

