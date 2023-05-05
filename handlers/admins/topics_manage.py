from aiogram import types
from aiogram.dispatcher import FSMContext
from data.config import ADMINS

from keyboards.inline import inline_buttons

from loader import bot, dp, db


@dp.message_handler(chat_id=-1001684447791)
async def bot_manage_topics(message: types.Update):
    thread_id = message.message_thread_id
    user = await db.get_topic(thread_id=thread_id)
    
    await bot.send_message(user.user_id, message.text)

    res = await db.get_last_question(user.user_id)
    await db.reg_conversation(user.user_id, res.title, res.question, message.text)