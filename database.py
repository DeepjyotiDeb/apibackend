from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import urllib

# host_server = os.environ.get('host_server', 'localhost')
# db_server_port = urllib.parse.quote_plus(str(os.environ.get('db_server_port', '5432')))
# database_name = os.environ.get('database_name', 'fastapi')
# db_username = urllib.parse.quote_plus(str(os.environ.get('db_username', 'postgres')))
# db_password = urllib.parse.quote_plus(str(os.environ.get('db_password', 'secret')))
# ssl_mode = urllib.parse.quote_plus(str(os.environ.get('ssl_mode','prefer')))
# DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(db_username, db_password, host_server, db_server_port, database_name, ssl_mode)

DATABASE_URL = 'postgresql://objwiguqrzqucf:d4b7bdaf3facc93f5cfc2b4eebbef34022b1eef808c40ea24683324406e695ac@ec2-52-19-164-214.eu-west-1.compute.amazonaws.com:5432/d90r8fbpb8achn'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind = engine, autocommit=False,autoflush= False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close