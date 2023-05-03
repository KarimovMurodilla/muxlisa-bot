from datetime import datetime
from distutils.sysconfig import get_makefile_filename
from sqlalchemy import Column, BigInteger, String, Integer, DateTime, Text

from utils.db_api.base import Base


class Users(Base):
    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)
    username = Column(String(50))
    first_name = Column(String(50))
    last_name = Column(String(50))


class Conversations(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True)
    title = Column(String(150))
    user_id = Column(BigInteger)
    question = Column(Text)
    answer = Column(Text)
    date = Column(DateTime, default=datetime.utcnow)


class Topics(Base):
    __tablename__ = "topics"

    user_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)
    message_thread_id = Column(Integer)