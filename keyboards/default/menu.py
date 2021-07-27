from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Продолжить")
        ],
        [
            KeyboardButton(text="Остановиться")
            KeyboardButton(text="Выйти")
        ],
    ],
    resize_keyboard=True
)
