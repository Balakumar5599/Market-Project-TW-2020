from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine

def db_connection():
    db_url = 'postgresql://postgres:Balagowtham11@localhost:5432/marketplace'
    sql_db = create_engine(db_url)
    db_session = scoped_session(sessionmaker(bind=sql_db))
    return db_session
