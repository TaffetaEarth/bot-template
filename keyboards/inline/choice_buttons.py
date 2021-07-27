from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline import callback_data
from keyboards.inline.callback_data import buy_callback

choice = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="Купить что-нибудь",
                                          callback_data=buy_callback.new(item_name="smt",
                                                                         quantity=1)
                                      )
                                      InlineKeyboardButton(
                                          text="Вернуться назад",
                                          callback_data="Return"
                                      )
                                  ]
                                  [
                                      InlineKeyboardButton(
                                          text="Отмена",
                                          callback_data="Cancel"
                                      )
                                  ]
                              )
