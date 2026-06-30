from sqlalchemy.orm import Session
from generator.event_generator import generate_event

def simulate_brute_force(
        db: Session, 
        username : str,
        ip_address : str
):
    events = []
    for _ in range(6):
        event = generate_event(
            db = db,
            username = username,
            ip_address = ip_address,
            event_type = "LOGIN_FAILED",
            resource = "/login"
        )
        events.append(event)
    return events

def simulate_resource_enumeration(db : Session, username : str, ip_address : str):
    events = []
    resources = [
        "/login",
        "/admin",
        "/dashboard",
        "/config",
        "/logs",
        "/users",
        "/reports",
        "/settings",
        "/metrics",
        "/api"
    ]
    for resource in resources:
        event = generate_event(
            db = db,
            username = username,
            ip_address = ip_address,
            event_type = "RESOURCE_ACCESS",
            resource = resource
        )
        events.append(event)
    return events

def simulate_credential_stuffing(db : Session, username : str, ip_address : str):
    events = []
    usernames = [
        "Luis",
        "Admin",
        "Pedro",
        "Maria",
        "Root"
    ]
    for user in usernames:
        event = generate_event(
            db = db,
            username = user,
            ip_address = ip_address,
            event_type = "LOGIN_FAILED",
            resource = "/login"
        )
        events.append(event)
    return events
