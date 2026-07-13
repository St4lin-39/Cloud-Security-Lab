def calculate_brute_force_confidence(attempts: int) -> int:
    if attempts >= 20:
        return 100
    elif attempts >= 12:
        return 90
    elif attempts >= 8:
        return 80
    return 70

def calculate_resource_enumeration_confidence(resources: int) -> int:
    if resources >= 15:
        return 100
    elif resources >= 10:
        return 85
    return 70

def calculate_credential_stuffing_confidence(users: int) -> int:
    if users >= 15:
        return 100
    elif users >= 10:
        return 95
    return 80

def calculate_password_spraying_confidence(users: int) -> int:
    if users >= 15:
        return 100
    elif users >= 10:
        return 95
    return 80

def calculate_multi_stage_attack_confidence(alerts: int) -> int:
    if alerts >= 5:
        return 100
    return 95