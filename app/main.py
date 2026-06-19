from database.connection import SessionLocal
from generator.event_generator import generate_event
from database.connection import Base, engine


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

    except Exception as e:
        print(f"Error: {e}")

    finally:
        db.close()


if __name__ == "__main__":
    main()