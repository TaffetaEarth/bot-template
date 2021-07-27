import types

from aiogram.dispatcher.filters import Command
from aiogram.types import User

from loader import dp, bot


@dp.message_handler(Command("inline_buttons_1"))
async def bot_father_func(message: types.Message):
    await message.answer(f"Edit @Sberleadbot info.\n"
                         f"Name: Бот для Заданий на Курсе Udemy\n"
                         f"Description: ?\n"
                         f"About: ?\n"
                         f"Botpic: ? no botpic\n"
                         f"Commands: no commands yet\n")
