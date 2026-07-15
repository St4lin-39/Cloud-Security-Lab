def calculate_priority(risk_score: int) -> str:
    if risk_score >= 80:
        return "URGENT"
    elif risk_score >= 60:
        return "HIGH"
    elif risk_score >= 40:
        return "MEDIUM"
    else:
        return "LOW"