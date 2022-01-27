from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import urllib
import os 

DATABASE_URL = os.environ.get('DATABASE_URL')
DATABASE_URL = DATABASE_URL[:8] + "ql" + DATABASE_URL[8:]
# host_server = os.environ.get('host_server', 'localhost')
# db_server_port = urllib.parse.quote_plus(str(os.environ.get('db_server_port', '5432')))
# database_name = os.environ.get('database_name', 'fastapi')
# db_username = urllib.parse.quote_plus(str(os.environ.get('db_username', 'postgres')))
# db_password = urllib.parse.quote_plus(str(os.environ.get('db_password', 'secret')))
# ssl_mode = urllib.parse.quote_plus(str(os.environ.get('ssl_mode','prefer')))
# DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(db_username, db_password, host_server, db_server_port, database_name, ssl_mode)

# DATABASE_URL = 'postgresql://bcousmwcngxnrr:27b77cee0eded7509d078d6c5cfef835beea60c66e5140d2991e043cd0beb010@ec2-63-32-30-191.eu-west-1.compute.amazonaws.com:5432/d970v91be4husa'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind = engine, autocommit=False,autoflush= False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close
