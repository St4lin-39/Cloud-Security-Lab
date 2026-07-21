from datetime import datetime
from models.alert_model import AlertModel
from config.alert_metadata import ALERT_METADATA
from services.confidence_engine import(
    calculate_brute_force_confidence,
    calculate_credential_stuffing_confidence,
    calculate_multi_stage_attack_confidence,
    calculate_password_spraying_confidence,
    calculate_resource_enumeration_confidence
)
from services.risk_engine import calculate_risk_score
from services.asset_criticality_engine import (
    get_asset_criticality,
    get_asset_criticality_score
)

def create_alert(
        alert_type: str,
        source_ip: str,
        attempts_volume: int,
        resource: str,
        username: str | None = None
):
    if alert_type == "BRUTE_FORCE_ATTEMPT":
        confidence = calculate_brute_force_confidence(attempts_volume)
    elif alert_type == "RESOURCE_ENUMERATION":
        confidence = calculate_resource_enumeration_confidence(attempts_volume)
    elif alert_type == "CREDENTIAL_STUFFING":
        confidence = calculate_credential_stuffing_confidence(attempts_volume)
    elif alert_type == "PASSWORD_SPRAYING":
        confidence = calculate_password_spraying_confidence(attempts_volume)
    elif alert_type == "MULTI_STAGE_ATTACK":
        confidence = calculate_multi_stage_attack_confidence(attempts_volume)
    else:
        confidence = 50
    
    
    metadata = ALERT_METADATA[alert_type]
    severity = metadata["severity"]
    asset_criticality = get_asset_criticality(resource)
    asset_criticality_score = get_asset_criticality_score(resource)
    risk_score = calculate_risk_score(
        severity,
        confidence,
        asset_criticality_score
    )
    return AlertModel(
        alert_type = alert_type,
        confidence = confidence,
        severity = severity,
        risk_score = risk_score,
        asset_criticality = asset_criticality,
        asset_criticality_score= asset_criticality_score,
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