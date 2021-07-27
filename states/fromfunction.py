from aiogram.dispatcher.filters.state import StatesGroup, State


class FromQuestions(StatesGroup):
    name = State()
    email = State()
    number = State()