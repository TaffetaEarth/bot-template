from aiogram.dispatcher.filters.state import StatesGroup, State


class BotFather(StatesGroup):
    command_to_father_bot = State()
    name_of_the_bot = State()
    value = State()