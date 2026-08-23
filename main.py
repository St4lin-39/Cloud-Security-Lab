from database.connection import (
    Base,
    engine,
    SessionLocal
)
from repositories.incident_timeline_repository import get_timeline_by_incident_id
from generator.attack_runner import (
    run_brute_force_attack, run_resource_enumeration_attack, run_credential_stuffing_attack, run_password_spraying_attack
)
from generator.simulation_data import get_password_spraying_password
from services.incident_engine import(
    get_open_incident_by_ip
)
from services.incident_lifecycle import incident_transition
def main():
    scenario = "INCIDENT_TEST"
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        if scenario == "BRUTE_FORCE":
            events, alerts = run_brute_force_attack(
                db=db,
                username="Luis",
                ip_address="192.168.1.100",
                attempts=6
            )

        elif scenario == "RESOURCE_ENUMERATION":
            resources = [
                "/login",
                "/register",
                "/dashboard",
                "/users",
                "/admin",
                "/config",
                "/reports",
                "/metrics",
                "/settings",
                "/api"
            ]
            events, alerts = run_resource_enumeration_attack(
                db = db,
                username = "luis",
                ip_address="192.168.100.1",
                resources= resources
            )
        elif scenario == "CREDENTIAL_STUFFING":
             usernames = [
                "Luis",
                "Carlos",
                "Ana",
                "Pedro",
                "Maria"
            ]

             events, alerts = run_credential_stuffing_attack(
                db=db,
                usernames = usernames,
                ip_address="192.168.1.100"
            )
        elif scenario == "PASSWORD_SPRAYING":
            usernames = [
                "Luis",
                "Carlos",
                "Ana",
                "Pedro",
                "Maria"
            ]
            spraying_password = get_password_spraying_password()
            events, alerts = run_password_spraying_attack(
                db = db,
                usernames = usernames,
                ip_address = "192.168.1.100",
                password_attempt= spraying_password
            )
        elif scenario == "INCIDENT_LIFECYCLE":

            incident = get_open_incident_by_ip(
                db=db,
                source_ip="192.168.1.100"
            )

            if incident is None:
                raise ValueError(
                    "No existe un incidente OPEN para probar el lifecycle"
                )

            print(f"Estado inicial: {incident.status}")

            incident = incident_transition(
                db=db,
                incident=incident,
                new_status="INVESTIGATING"
            )

            print(f"Estado actual: {incident.status}")

            incident = incident_transition(
                db=db,
                incident=incident,
                new_status="CONTAINED"
            )

            print(f"Estado actual: {incident.status}")

            incident = incident_transition(
                db=db,
                incident=incident,
                new_status="CLOSED"
            )

            print(f"Estado final: {incident.status}")

            events = []
            alerts = []
        elif scenario == "CORRELATION":

            events = []
            alerts = []

            brute_events, brute_alerts = run_brute_force_attack(
                db=db,
                username="Luis",
                ip_address="192.168.1.100",
                attempts=6
            )

            events.extend(brute_events)
            alerts.extend(brute_alerts)

            resources = [
                "/login",
                "/dashboard",
                "/users",
                "/admin",
                "/config",
                "/metrics"
            ]

            resource_events, resource_alerts = run_resource_enumeration_attack(
                db=db,
                username="Luis",
                ip_address="192.168.1.100",
                resources=resources
            )

            events.extend(resource_events)
            alerts.extend(resource_alerts)

            usernames = [
                "Luis",
                "Carlos",
                "Ana",
                "Pedro",
                "Maria"
            ]

            credential_events, credential_alerts = run_credential_stuffing_attack(
                db=db,
                usernames=usernames,
                ip_address="192.168.1.100"
            )

            events.extend(credential_events)
            alerts.extend(credential_alerts)

        elif scenario == "INCIDENT_TEST":

            events = []
            alerts = []

            brute_events, brute_alerts = run_brute_force_attack(
                db=db,
                username="Luis",
                ip_address="192.168.1.100",
                attempts=6
            )

            events.extend(brute_events)
            alerts.extend(brute_alerts)

            incident = get_open_incident_by_ip(
                db=db,
                source_ip="192.168.1.100"
            )

            if incident is None:
                raise ValueError(
                    "No existe un incidente OPEN para probar el lifecycle"
                )

            print("\n===== INCIDENTE =====")
            print(f"Estado: {incident.status}")
            print(f"Clasificación: {incident.classification}")
            print(f"Prioridad: {incident.priority}")
            print(f"Risk Score: {incident.risk_score}")
            print(f"Alertas asociadas: {incident.alerts_count}")

            incident = incident_transition(
                db=db,
                incident=incident,
                new_status="INVESTIGATING"
            )

            incident = incident_transition(
                db=db,
                incident=incident,
                new_status="CONTAINED"
            )

            incident = incident_transition(
                db=db,
                incident=incident,
                new_status="CLOSED"
            )

            print("\n===== TIMELINE =====")

            timeline = get_timeline_by_incident_id(
                db=db,
                incident_id=incident.id
            )

            for event in timeline:
                print(
                    f"{event.created_at} | "
                    f"{event.event_type} | "
                    f"{event.description}"
        )
        else:
            raise ValueError("Tipo de ataque no soportado")

        print(f"\nEventos generados: {len(events)}")
        print(f"Alertas generadas: {len(alerts)}")

        for alert in alerts:
            print(f"{alert.alert_type} | " f"{alert.username} | " f"{alert.source_ip}")
    
    finally:
        db.close()

if __name__ == "__main__":
    main()