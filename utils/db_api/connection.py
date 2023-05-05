import asyncio
from typing import Sequence
from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession

from utils.db_api.base import Base
from utils.db_api.models import (
    Users, Conversations, 
    Topics, WaitList
    )

from data.config import DATABASE_URL


class Database:
    def get_engine(self):
        engine = create_async_engine(
            DATABASE_URL,
            future=True
        )

        return engine

    async def load(self) -> AsyncSession:
        engine= self.get_engine()
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        async_sessionmaker = sessionmaker(
            engine, expire_on_commit=False, class_=AsyncSession
        )

        self.async_session = async_sessionmaker

    # ---Users model---

    async def reg_user(self, user_id: str, username: str, first_name: str):
        """Регистрация пользователя"""
        async with self.async_session() as session:
            session: AsyncSession
            await session.merge(
                Users(
                    user_id=user_id,
                    username=username,
                    first_name=first_name
                )
            )
            await session.commit()

    async def get_user(self, user_id) -> Users:
        """Получения пользователя"""
        async with self.async_session() as session:
            session: AsyncSession

            response = await session.get(Users, user_id)
            return response
    
    async def get_all_users(self) -> Sequence[Users]:
        """Получения всех пользователей"""
        async with self.async_session() as session:
            session: AsyncSession

            response = await session.execute(select(Users))
            return response.scalars().all()
        

    # ---Forums model---    
    async def reg_topic(self, user_id, thread_id):
        async with self.async_session() as session:
            session: AsyncSession
            await session.merge(
                Topics(
                    user_id=user_id,
                    message_thread_id=thread_id
                )
            )
            await session.commit()

    async def get_topic(self, user_id = None, thread_id = None) -> Topics:
        async with self.async_session() as session:
            session: AsyncSession

            if user_id:
                response = await session.get(Topics, user_id)
                return response

            elif thread_id:
                response = await session.execute(select(Topics).where(Topics.message_thread_id == thread_id))
                return response.scalar()


    # ---WaitList---
    async def reg_question(self, user_id, title, question):
        async with self.async_session() as session:
            session: AsyncSession
            await session.merge(
                WaitList(
                    user_id=user_id,
                    title=title,
                    question=question
                )
            )
            await session.commit()
    
    async def get_last_question(self, user_id):
        async with self.async_session() as session:
            stmt = select(WaitList).where(WaitList.user_id == user_id).order_by(WaitList.id.desc())
            result = await session.execute(stmt)
            first_value = result.scalars().first()
        
        return first_value


    # ---Conversations model---
    async def reg_conversation(self, user_id, title, question, answer=None):
        async with self.async_session() as session:
            session: AsyncSession
            obj = await session.merge(
                Conversations(
                    user_id=user_id,
                    title=title,
                    question=question,
                    answer=answer
                )
            )
            await session.commit()
        
        return obj