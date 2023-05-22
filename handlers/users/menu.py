from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.default import kb_menu
from loader import dp

@dp.message_handler(Command("menu"))
@dp.message_handler(text = 'Главное меню')
async def menu(message: types.Message):
    await message.answer("Вы попали в меню.", reply_markup=kb_menu)