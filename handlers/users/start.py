from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline import inline_buttons
from keyboards.default import keyboard_buttons

from loader import dp, db


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        "Assalomu aleykum!\n"
        "Yangi suhbatni boshlash uchun /chat komandasini yuboring!"
    )