from sqlalchemy.orm import Session
from entities.incident_entity import IncidentTable
from models.incident_model import IncidentModel


def save_incident(db : Session, incident_model : IncidentModel):
    try:
        incident = IncidentTable(
            incident_type = incident_model.incident_type,
            classification = incident_model.classification,
            classification_score = incident_model.classification_score,
            severity = incident_model.severity,
            priority = incident_model.priority,
            status = incident_model.status,
            risk_score = incident_model.risk_score,
            asset_criticality = incident_model.asset_criticality,
            asset_criticality_score = incident_model.asset_criticality_score,
            source_ip = incident_model.source_ip,
            alerts_count = incident_model.alerts_count,
            first_seen = incident_model.first_seen,
            last_seen = incident_model.last_seen
        )
        db.add(incident)
        db.commit()
        db.refresh(incident)
        return incident
    except Exception:
        db.rollback()
        raise

def get_open_incident_by_ip(db : Session, source_ip : str):
    return (db.query(IncidentTable).filter(IncidentTable.source_ip == source_ip).filter(IncidentTable.status == "OPEN").first())

def count_incidents(db : Session):
    return (db.query(IncidentTable).count())

def update_incident(db: Session, incident : IncidentTable):
    try:
        db.commit()
        db.refresh(incident)
        return incident
    except Exception:
        db.rollback()
        raise

def get_all_incidents(db: Session):
    return (db.query(IncidentTable).all())