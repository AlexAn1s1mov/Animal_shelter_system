import logging

from aiogram import Dispatcher

from data.config import admins
from keyboards.default import kb_menu


async def on_startup_notify(dp: Dispatcher):
    for admin in admins:
        try:
            text = 'Бот запущен'
            await dp.bot.send_message(chat_id=admin, text=text, reply_markup=kb_menu)
        except Exception as err:
            logging.exception(err)
