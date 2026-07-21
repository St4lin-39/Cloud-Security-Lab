from datetime import datetime
from models.alert_model import AlertModel
from models.incident_model import IncidentModel
from sqlalchemy.orm import Session 
from repositories.incident_repository import(
    save_incident,
    update_incident,
    get_open_incident_by_ip
)
from services.priority_engine import calculate_priority
from config.incident_mapping import INCIDENT_MAPPING
from entities.incident_entity import IncidentTable
from config.asset_criticality import ASSET_CRITICALITY


SEVERITY_ORDER = {
    "LOW" : 1,
    "MEDIUM" : 2,
    "HIGH" : 3,
    "CRITICAL" : 4
}
def create_incident(db: Session, alert : AlertModel):
    incident_type = INCIDENT_MAPPING[alert.alert_type]
    priority = calculate_priority(
        alert.risk_score
    )
    current_time = datetime.utcnow()
    incident = IncidentModel(
        incident_type= incident_type,
        severity = alert.severity,
        priority= priority,
        status = "OPEN",
        risk_score= alert.risk_score,
        asset_criticality = alert.asset_criticality,
        asset_criticality_score= alert.asset_criticality_score,
        source_ip= alert.source_ip,
        alerts_count= 1,
        first_seen = current_time,
        last_seen = current_time
    )
    return save_incident(
        db = db,
        incident_model= incident
    )

def update_existing_incident(db : Session, incident: IncidentTable, alert: AlertModel):
    incident.alerts_count += 1
    incident.last_seen = datetime.utcnow()
    incident.risk_score = max(
        incident.risk_score,
        alert.risk_score
    )
    incident.priority = calculate_priority(
        incident.risk_score
    )
    if(SEVERITY_ORDER[alert.severity] > SEVERITY_ORDER[incident.severity]):
        incident.severity = alert.severity
    if (
        alert.asset_criticality_score
        > incident.asset_criticality_score
    ):
        incident.asset_criticality = alert.asset_criticality
        incident.asset_criticality_score = (
            alert.asset_criticality_score
        )
    if alert.alert_type == "MULTI_STAGE_ATTACK":
        incident.incident_type = INCIDENT_MAPPING[
            alert.alert_type
        ]
    return update_incident(
        db = db,
        incident = incident
    )

def process_incident(db: Session, alert : AlertModel):
    incident = get_open_incident_by_ip(
        db = db,
        source_ip= alert.source_ip
    )
    if incident is None:
        return create_incident(
            db= db,
            alert = alert
        )
    return update_existing_incident(
        db = db,
        incident = incident,
        alert = alert
    )