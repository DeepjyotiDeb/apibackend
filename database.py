from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgres://objwiguqrzqucf:d4b7bdaf3facc93f5cfc2b4eebbef34022b1eef808c40ea24683324406e695ac@ec2-52-19-164-214.eu-'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind = engine, autocommit=False,autoflush= False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close