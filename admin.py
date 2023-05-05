import asyncio
from fastapi import FastAPI
from sqladmin import Admin, ModelView

from utils.db_api.models import (
    Users, Conversations, 
    Topics, WaitList
    )

from loader import db

engine = db.get_engine()

app = FastAPI()
admin = Admin(app, engine)


class UserAdmin(ModelView, model=Users):
    column_list = [Users.user_id, Users.username, Users.first_name, Users.last_name]


class ConversationsAdmin(ModelView, model=Conversations):
    column_list = [
        Conversations.id, Conversations.user_id, Conversations.title, 
        Conversations.question, Conversations.answer, Conversations.date
    ]

   
class TopicsAdmin(ModelView, model=Topics):
    column_list = [Topics.user_id, Topics.message_thread_id]

   
class WaitListAdmin(ModelView, model=WaitList):
    column_list = [
        WaitList.id, WaitList.user_id, 
        WaitList.title, WaitList.question
    ]

   

admin.add_view(UserAdmin)
admin.add_view(ConversationsAdmin)
admin.add_view(TopicsAdmin)
admin.add_view(WaitListAdmin)