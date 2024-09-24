from app.database.database import SessionLocal
from app.database.seeders import run_seeders

if __name__ == "__main__":
    db = SessionLocal()
    run_seeders(db)