from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from states.bundle import Bundle
from keyboards.default import keyboard_buttons
from loader import bot, dp, db


@dp.message_handler(commands='chat', state='*')
async def bot_new_chat(message: types.Message, state: FSMContext):
    await message.answer("Kategoriyani tanlang:", reply_markup=keyboard_buttons.categories())
    await Bundle.step1.set()


@dp.message_handler(state=Bundle.step1)
async def bot_new_chat(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text
        
    await message.answer("So'rovingizni yuboring", reply_markup=keyboard_buttons.categories())
    await Bundle.next()


@dp.message_handler(state=Bundle.step2)
async def receiver(message: types.Message):
    user = message.from_user
    topic = await db.get_topic(user.id)

    if not topic:
        forum = await bot.create_forum_topic(-1001684447791, user.first_name)
        await bot.send_message(
            chat_id=-1001684447791,
            text=message.text,
            message_thread_id=forum.message_thread_id
        )
        await db.reg_topic(user.id, forum.message_thread_id)
    
    else:
        await bot.send_message(
            chat_id=-1001684447791,
            text=message.text,
            message_thread_id=topic.message_thread_id
        )