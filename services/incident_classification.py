from config.incident_classification import (
    CLASSIFICATION_SCORES,
    classify_incident
)


def calculate_classification_score(
    current_score: int,
    alert_type: str
) -> int:

    alert_score = CLASSIFICATION_SCORES.get(
        alert_type,
        0
    )

    return current_score + alert_score


def calculate_classification_confidence(
    classification_score: int
) -> str:

    if classification_score >= 55:
        return "HIGH"

    if classification_score >= 30:
        return "MEDIUM"

    return "LOW"


def classify(
    classification_score: int,
    has_successful_login: bool,
    has_sensitive_access: bool
) -> tuple[str, str]:

    classification = classify_incident(
        classification_score=classification_score,
        has_successful_login=has_successful_login,
        has_sensitive_access=has_sensitive_access
    )

    confidence = calculate_classification_confidence(
        classification_score
    )

    return classification, confidence