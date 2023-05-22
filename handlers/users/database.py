from aiogram import types

from data.config import admins
from handlers.utils.db_api.query.animals_q import *
from loader import dp
from keyboards.default import kb_db, kb_db_admin, kb_db_tools


cur_table = ''

@dp.message_handler(text='База данных')
async def data_base(message: types.Message):
    await message.answer(f'Что вы хотите сделать?', reply_markup=kb_db)

@dp.message_handler(text='Работа с базой данных')
async def data_base(message: types.Message):
    if message.from_user.id in admins:
        await message.answer(f'Выберите таблицу', reply_markup=kb_db_admin)
    else:
        await message.answer(f'У вас не хватает прав доступа!')

                                                    # Animals
@dp.message_handler(text='Животные')
async def animals_select(message: types.Message):
    if message.from_user.id in admins:
        global cur_table
        cur_table = 'Животные'

        await message.answer("Вы выбрали таблицу 'Животные'.", reply_markup=kb_db_tools)


@dp.message_handler(text='Просмотреть')
async def animals_select(message: types.Message):
    if message.from_user.id in admins:
        global cur_table
        if cur_table == 'Животные':
            await message.answer(f'Содержимое таблицы:\n {select_all_animals()}')



