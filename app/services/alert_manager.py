from models.alert_model import AlertModel
from sqlalchemy.orm import Session
from repositories.alert_repository import has_recent_alert, save_alert

def process_alert(db : Session, alert_model : AlertModel):
    recent_alert_exists = has_recent_alert(db, alert_model.alert_type, alert_model.source_ip)
    if recent_alert_exists == True:
        return None
    else:
        saved_alert = save_alert(db = db, alert_model=alert_model)
        return saved_alert