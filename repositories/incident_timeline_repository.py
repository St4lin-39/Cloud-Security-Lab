from entities.incident_timeline_entity import IncidentTimelineTable

def save_incident_timeline(db, timeline_model):
    timeline = IncidentTimelineTable(
        id = timeline_model.id,
        incident_id = timeline_model.incident_id,
        event_type = timeline_model.event_type,
        description = timeline_model.description,
        created_at = timeline_model.created_at
    )
    db.add(timeline)
    db.commit()
    db.refresh(timeline)

    return timeline

def get_timeline_by_incident_id(db, incident_id : int):
    return(db.query(IncidentTimelineTable).filter(IncidentTimelineTable.incident_id == incident_id).order_by(IncidentTimelineTable.created_at).all())

