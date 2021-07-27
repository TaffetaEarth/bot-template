from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class FromFilter(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return (message.text == "/form@person_assist_bot" or message.text == "/form")
