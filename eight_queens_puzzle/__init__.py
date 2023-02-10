from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

from .models import Base


# Configure connection through the environment
load_dotenv()
engine = create_engine("postgresql+psycopg2cffi://", future=True)
Session = sessionmaker(engine)


def create_tables():
    Base.metadata.create_all(engine)


def drop_tables():
    Base.metadata.drop_all(engine)
