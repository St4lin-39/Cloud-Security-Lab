from database.connection import (
    Base,
    engine,
    SessionLocal
)

from generator.attack_runner import (
    run_brute_force_attack, run_resource_enumeration_attack, run_credential_stuffing_attack
)


def main():
    attack_type = "CREDENTIAL_STUFFING"
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        if attack_type == "BRUTE_FORCE":
            events, alerts = run_brute_force_attack(
                db=db,
                username="Luis",
                ip_address="192.168.1.100",
                attempts=6
            )

        elif attack_type == "RESOURCE_ENUMERATION":
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
        elif attack_type == "CREDENTIAL_STUFFING":
             usernames = [
                "Luis",
                "Carlos",
                "Ana",
                "Pedro",
                "Maria"
            ]

             events, alerts = run_credential_stuffing_attack(
                db=db,
                username= usernames,
                ip_address="192.168.1.100"
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