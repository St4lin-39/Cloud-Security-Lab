from datetime import datetime
from models.incident_timeline_model import IncidentTimelineModel
from repositories.incident_timeline_repository import save_incident_timeline

def create_timeline(
        db,
        incident_id : int,
        event_type : str,
        description : str
):
    timeline = IncidentTimelineModel(
        incident_id=incident_id,
        event_type=event_type,
        description=description,
        created_at= datetime.utcnow()
    )
    return save_incident_timeline(
        db = db,
        timeline_model = timeline
    )

