from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.default import kb_menu
from loader import dp


@dp.message_handler(text = 'Контакты')
async def contacts(message: types.Message):
    await message.answer("Будем рады Вашему обращению!\n"
                         "Телефон: +7-915-016-77-61")