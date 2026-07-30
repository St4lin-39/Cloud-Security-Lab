CLASSIFICATION_SCORES = {
    "BRUTE_FORCE_ATTEMPT": 10,
    "PASSWORD_SPRAYING": 15,
    "CREDENTIAL_STUFFING": 15,
    "RESOURCE_ENUMERATION": 10,
    "LOGIN_SUCCESS": 30,
    "SENSITIVE_RESOURCE_ACCESS": 25,
}

CLASSIFICATION_THRESHOLDS = {
    "ACCOUNT_COMPROMISE": 30,
    "DATA_BREACH": 55,
}

def classify_incident(
    classification_score: int,
    has_successful_login: bool,
    has_sensitive_access: bool
):

    if (
        has_sensitive_access
        and classification_score >= CLASSIFICATION_THRESHOLDS["DATA_BREACH"]
    ):
        return "DATA_BREACH"

    if (
        has_successful_login
        and classification_score >= CLASSIFICATION_THRESHOLDS["ACCOUNT_COMPROMISE"]
    ):
        return "ACCOUNT_COMPROMISE"

    return "CREDENTIAL_ATTACK"