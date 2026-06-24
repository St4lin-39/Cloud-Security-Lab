from database.connection import (
    Base,
    engine,
    SessionLocal
)

from generator.attack_runner import (
    run_brute_force_attack
)


def main():

    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:

        events, alerts = run_brute_force_attack(
            db=db,
            username="Luis",
            ip_address="192.168.1.100",
            attempts=6
        )

        print(
            f"Eventos generados: {len(events)}"
        )

        print(
            f"Alertas generadas: {len(alerts)}"
        )

    except Exception as e:

        print(
            f"Error: {e}"
        )

    finally:

        db.close()


if __name__ == "__main__":
    main()