import os
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL not set in environment")

# Neon optimization: 
# 1. Use connect_args for faster connection setup if needed
# 2. Increase pool size if many requests are happening
engine = create_engine(
    DATABASE_URL, 
    echo=False, # Set to False to reduce log clutter
    pool_pre_ping=True, # Ensure connection is alive before using
    pool_size=5,
    max_overflow=10
)

def get_session():
    with Session(engine) as session:
        yield session

def init_db():
    # Tables exist, but this will ensure they match our current models
    SQLModel.metadata.create_all(engine)
