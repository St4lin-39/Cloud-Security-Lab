from repositories.incident_repository import update_incident
VALID_TRANSITIONS = {
    "OPEN" : ["INVESTIGATING", "CLOSED"],
    "INVESTIGATING" : ["CONTAINED", "CLOSED"],
    "CONTAINED" : ["CLOSED"],
    "CLOSED" : []
}

def incident_transition(
        db,
        incident,
        new_status : str
):
    current_status = incident.status
    if new_status not in VALID_TRANSITIONS.get(
        current_status,
        []
    ):
        raise ValueError(
            f"Invalid incident transition: "
            f"{current_status} -> {new_status}"
        )
    
    incident.status = new_status

    return update_incident(
        db = db,
        incident = incident
    )