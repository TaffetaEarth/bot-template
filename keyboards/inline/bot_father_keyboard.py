from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.bot_father_data import bot_father_call

bot_father_call = InlineKeyboardMarkup(row_width=2,
                                       inline_keyboard=[
                                           [InlineKeyboardButton(
                                               text="Edit Name",
                                               callback_data=bot_father_call.new(call="name_change")
                                           )
                                           ]
                                       ]
                                       )
