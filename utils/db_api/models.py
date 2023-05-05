from sqlalchemy.orm import relationship

from datetime import datetime
from distutils.sysconfig import get_makefile_filename
from sqlalchemy import (
    Column, BigInteger, 
    String, Integer, 
    DateTime, Text, ForeignKey
    )

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
    user_id = Column(BigInteger)
    title = Column(String(150))
    question = Column(Text)
    answer = Column(Text)
    date = Column(DateTime, default=datetime.utcnow)


class WaitList(Base):
    __tablename__ = "wait_list"

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)
    title = Column(String(150))
    question = Column(Text)


# class Answers(Base):
#     __tablename__ = "answers"

#     id = Column(Integer, primary_key=True)
#     answer = Column(Text)
#     conversation_id = Column(Integer, ForeignKey('conversations.id'), nullable=False)


class Topics(Base):
    __tablename__ = "topics"

    user_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)
    message_thread_id = Column(Integer)