SEVERITY_SCORE = {
    "LOW": 20,
    "MEDIUM" : 50,
    "HIGH" : 75,
    "CRITICAL" : 100
}

def calculate_risk_score(severity: str, confidence: int, asset_criticality_score : int) -> int:
    severity_value = SEVERITY_SCORE[severity]
    risk = (severity_value * 0.4) + (confidence * 0.3) + (asset_criticality_score * 0.3)
    return round(risk)

