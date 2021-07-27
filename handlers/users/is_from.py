from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters import state, Command

from filters.is_from import FromFilter
from loader import dp
from states.fromfunction import FromQuestions


@dp.message_handler(Command("form"))
async def bot_answer_to_from(message: types.Message):
    await message.answer(f"Привет! Введите, пожалуйста, свое имя:")
    await FromQuestions.first()


@dp.message_handler(state=FromQuestions.name)
async def name_of_user(message: types.Message, state: FSMContext):
    name = message.text
    async with state.proxy() as data:
        data["name"] = name
    await message.answer(f"Введите, пожалуйста, свой e-mail:")
    await FromQuestions.next()


@dp.message_handler(state=FromQuestions.email)
async def e_mail_of_user(message: types.Message, state: FSMContext):
    email = message.text
    async with state.proxy() as data:
        data["email"] = email
    await message.answer(f"Введите, пожалуйста, свой телефон:")
    await FromQuestions.next()


@dp.message_handler(state=FromQuestions.number)
async def phone_number_of_user(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    email = data.get("email")
    phone_number = message.text
    await message.answer(f"Привет! Ты ввел следующие данные: \n"
                         f"Имя - {name} \n"
                         f"Email - {email} \n"
                         f"Телефон: - {phone_number}")

    await state.finish()
