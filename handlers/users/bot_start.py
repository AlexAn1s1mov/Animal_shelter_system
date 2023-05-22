from aiogram import types

from data.config import admins
from handlers.utils.db_api import quick_commands as commands
from keyboards.default import kb_menu
from loader import dp

@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    try:
        user = await commands.select_user(message.from_user.id)
        if user.status == 'active':
            await message.answer(f'Привет {user.first_name}\n'
                                 f'Ты уже зарегистрирован', reply_markup=kb_menu)
        elif user.status == 'baned':
            await message.answer('Ты забанен')
    except Exception:
        await commands.add_user(user_id=message.from_user.id,
                                first_name=message.from_user.first_name,
                                last_name=message.from_user.last_name,
                                username=message.from_user.username,
                                status='active')
        await message.answer(f'Привет {message.from_user.full_name}\n'
                                 f'Ты зарегистрирован', reply_markup=kb_menu)

@dp.message_handler(text='/ban', chat_id=admins)
async def get_ban(message: types.Message):
    await commands.update_status(user_id=message.from_user.id, status='baned')
    await message.answer('Мы тебя забанили')

@dp.message_handler(text='/unban', chat_id=admins)
async def get_ban(message: types.Message):
    await commands.update_status(user_id=message.from_user.id, status='active')
    await message.answer('Ты больше не забанен')

@dp.message_handler(text='/profile')
async def get_ban(message: types.Message):
    user = await commands.select_user(message.from_user.id)
    await message.answer(f'ID - {user.user_id}\n'
                         f'first_name - {user.first_name}\n'
                         f'last_name - {user.last_name}\n'
                         f'username - {user.username}\n'
                         f'status - {user.status}')