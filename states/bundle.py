from aiogram.dispatcher.filters.state import State, StatesGroup


class Bundle(StatesGroup):
	step1 = State()
	step2 = State()