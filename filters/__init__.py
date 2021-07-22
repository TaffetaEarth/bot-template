from aiogram import Dispatcher
from filters.is_from import FromFilter
from loader import dp
# from .is_admin import AdminFilter


if __name__ == "filters":
    #dp.filters_factory.bind(is_admin)
    dp.filters_factory.bind(FromFilter)
    pass

