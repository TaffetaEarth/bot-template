from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from aiogram import types

from states import Test


@dp.message_handler(Command("test"))
async def enter_text(message: types.Message):
    await message.answer('Вы начали тестирование \n'
                         "Вопрос номер 1: .... \n")


await Test.q1.set()
# await Test.first()

@dp.message_handler(state=Test.q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

