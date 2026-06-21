from database.connection import SessionLocal
from generator.event_generator import generate_event
from database.connection import Base, engine
from detection.detection_engine import detect_brute_force
from repositories.alert_repository import save_alert


def main():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        event = generate_event(
            db=db,
            username="Luis",
            ip_address="192.168.1.100",
            event_type="LOGIN_FAILED",
            resource="/login"
        )

        print(f"Evento guardado correctamente: {event.id}")

        alert = detect_brute_force(
            db, event.username, event.ip_address
        )
        if alert:
            saved_alert = save_alert(
                db = db,
                alert_model = alert
            )
            print(f"Alerta generada: {saved_alert.alert_type}")
        else:
            print("No se detecto actividad sospechosa")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        db.close()


if __name__ == "__main__":
    main()