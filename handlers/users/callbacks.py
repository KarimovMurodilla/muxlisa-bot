from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, db
from keyboards.inline import inline_buttons


@dp.callback_query_handler(state ='*')
async def queryFunc(c: types.CallbackQuery, state: FSMContext):
    pass