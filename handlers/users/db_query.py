from aiogram import types
from aiogram.dispatcher import FSMContext

from states.st_animal_query import state_animal_q
from data.config import admins
from handlers.utils.db_api.query.animals_q import *
from loader import dp, bot
from keyboards.default import *
from handlers.utils.db_api.query import *
from handlers.utils.qr_code import read_qr
import pandas as pd
import psycopg2
import datetime
from datetime import date
from psycopg2 import Error
import warnings
warnings.simplefilter("ignore")

def id_animal_select(id):
    try:
        # Подключение к базе данных
        conn = psycopg2.connect(
            dbname='dog_shelter',
            user='postgres',
            password='Alex2001',
            host='localhost')

        # Извлечение данных из таблицы
        sql_zap = '''SELECT kind, name, sex, date_of_birth, enclosure_id, status
         FROM animals
        where id = {}'''.format(id)
        zapros = pd.read_sql(sql_zap, conn)
        # df = pd.DataFrame(zapros)


        # Закрытие соединения
        #conn.close()
        # Закрытие соединения
        return(zapros)

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if conn:
            conn.close()

# @dp.message_handler(text='О животном')
# async def id_animal_info(message: types.Message):
#     await message.answer(f"Пришлите QR-код собаки")
#     @dp.message_handler(content_types=[types.ContentType.PHOTO])
#     async def download_photo_3(message: types.Message):
#         await message.photo[-1].download()
#         img_path = (await bot.get_file(message.photo[-1].file_id)).file_path
#         data = id_animal_select(read_qr(img_path))
#         await message.answer(f'Тип: {data["kind"][0]}\n'
#                              f'Кличка: {data["name"][0]}\n'
#                              f'Пол: {data["sex"][0]}\n'
#                   f'Номер вольера: {data["enclosure_id"][0]}\n'
#                              f'Статус: : {data["status"][0]}')
# #         # await message.answer(f'{data}')               f'Дата рождения: {data["date_of_birth"][0]}\n'
#

@dp.message_handler(text='О животном')
async def info_animal(message: types.Message):
    await message.answer(f"Пришлите QR-код собаки")
    await state_animal_q.first()
@dp.message_handler(state=state_animal_q.answer1,content_types=[types.ContentType.PHOTO])
async def state1(message: types.Message, state: FSMContext):
    await message.photo[-1].download()
    img_path = (await bot.get_file(message.photo[-1].file_id)).file_path
    data = id_animal_select(read_qr(img_path))
    await message.answer(f'Тип: {data["kind"][0]}\n'
                         f'Кличка: {data["name"][0]}\n'
                         f'Пол: {data["sex"][0]}\n'
                         f'Номер вольера: {data["enclosure_id"][0]}\n'
                         f'Статус: : {data["status"][0]}')
    # await message.answer(f'{data["kind"][0]}')

    await state.update_data(answer1 = img_path)
    data = await state.get_state()
    if data != None:
        await state.finish()
def count_dogs():
    try:
        # Подключение к базе данных
        conn = psycopg2.connect(
            dbname='dog_shelter',
            user='postgres',
            password='Alex2001',
            host='localhost')

        # Извлечение данных из таблицы
        sql_zap = '''SELECT count(*) FROM animals
        where kind = 'собака' and date_of_exit is null
        '''
        zapros = pd.read_sql(sql_zap, conn)
        #df = pd.DataFrame(zapros)

        # Закрытие соединения
        conn.close()
        # Закрытие соединения
        return(zapros)

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if conn:
            conn.close()

@dp.message_handler(text='Количество собак в приюте')
async def id_animal_info(message: types.Message):
    await message.answer(f'В приюте {count_dogs()["count"][0]} собак')
