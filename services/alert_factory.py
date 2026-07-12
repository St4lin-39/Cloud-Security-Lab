from datetime import datetime
from models.alert_model import AlertModel
from config.alert_metadata import ALERT_METADATA

def create_alert(
        alert_type: str,
        source_ip: str,
        attempts_volume: int,
        username: str | None = None
):
    metadata = ALERT_METADATA[alert_type]
    return AlertModel(
        alert_type = alert_type,
        severity = metadata["severity"],
        confidence = metadata["confidence"],
        status = "OPEN",
        description = metadata["description"],
        recommendation = metadata["recommendation"],
        mitre_tactic= metadata["mitre_tactic"],
        mitre_technique= metadata["mitre_technique"],
        username = username,
        source_ip = source_ip,
        attempts_volume = attempts_volume,
        created_at = datetime.utcnow()
    )