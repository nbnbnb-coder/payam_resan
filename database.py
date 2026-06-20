from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://chatdb_bf6r_user:fDsW6jZXh2KZ7HcDaeU6WyMCNDMfyFzr@dpg-d8ra9n36sc1c73b0sm70-a.oregon-postgres.render.com/chatdb_bf6r"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
