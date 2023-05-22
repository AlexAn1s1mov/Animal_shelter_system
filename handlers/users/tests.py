from aiogram import types
from loader import dp
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


# @dp.message_handler(text=['Привет', 'привет', 'Hi', 'hi', 'Hello', 'hello'])
# async def command_hello(message: types.Message):
#     await message.answer(f'Привет {message.from_user.full_name}!')

@dp.message_handler(text="inline_url")
async def cmd_inline_url(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="GitHub", url="https://github.com"),
        types.InlineKeyboardButton(text="Оф. канал Telegram", url="tg://resolve?domain=telegram")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Кнопки-ссылки", reply_markup=keyboard)
