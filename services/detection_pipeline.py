from sqlalchemy.orm import Session

from detection.detection_engine import run_detection_engine
from correlation.correlation_engine import correlate_alerts
from services.alert_manager import process_alert
from services.incident_engine import process_incident

def process_event(db: Session, event):

    generated_alerts = []

   
    alerts = run_detection_engine(
        db=db,
        event=event
    )

    for alert in alerts:

        saved_alert = process_alert(
            db=db,
            alert_model=alert
        )

        if saved_alert:
            process_incident(
                db = db,
                alert = saved_alert
            )
            generated_alerts.append(saved_alert)

    correlated_alert = correlate_alerts(
        db=db,
        source_ip=event.ip_address,
        resource = event.resource
    )

    if correlated_alert:

        saved_correlated_alert = process_alert(
            db=db,
            alert_model=correlated_alert
        )

        if saved_correlated_alert:
            process_incident(
                db = db,
                alert = saved_correlated_alert
            )
            generated_alerts.append(saved_correlated_alert)

    return generated_alerts