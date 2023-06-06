# from aiogram import types
# from aiogram.dispatcher import FSMContext
#
# from data.config import admins
# from handlers.utils.qr_code import read_qr
# from aiogram import Bot, Dispatcher, executor, types
#
# from Classifier.train import ResNet50_predict_breed, train_model
# from keyboards.default import kb_menu
# from keyboards.default.keyboard_menu import kb_menu_2
# from loader import dp, bot
# import pandas as pd
# import psycopg2
# import datetime
# from datetime import date
# from psycopg2 import Error
# import warnings
# warnings.simplefilter("ignore")
#
# def add_walk(img, id):
#     conn = psycopg2.connect(
#         dbname='dog_shelter',
#         user='postgres',
#         password='Alex2001',
#         host='localhost')
#
#     cursor = conn.cursor()
#     # Извлечение данных из таблицы
#     sql_zap = '''SELECT * FROM walks'''
#     zapros = pd.read_sql(sql_zap, conn)
#
#     current_date = date.today()
#     #print(current_date)
#
#     current_date_time = datetime.datetime.now()
#     current_time = current_date_time.time()
#     #print(current_time)
#
#     read_qr(img)
#     cursor.execute('''INSERT INTO walks (id, date_of_walk, time_start, animal_id)
#         VALUES (%s, %s, %s, %s)''',
#                    (len(zapros), current_date, current_time, read_qr(img)))
#     conn.commit()
#
#     cursor.execute('''INSERT INTO walks_members (id, walk_id, volonture_id)
#         VALUES (%s, %s, %s)''',
#                    (len(zapros), len(zapros), id))
#     conn.commit()
#     # Закрытие соединения
#     cursor.close()
#     conn.close()
#
# img_path=''
# @dp.message_handler(text="Выйти на прогулку")
# async def create_walk(message: types.Message):
#     await message.answer(f"Пришлите QR-код собаки")
#     @dp.message_handler(content_types=[types.ContentType.PHOTO])
#     async def download_photo(message: types.Message):
#         await message.photo[-1].download()
#         global img_path
#         img_path = (await bot.get_file(message.photo[-1].file_id)).file_path
#     add_walk(img_path, message.from_user.id)
#     await message.answer(f"Хорошей прогулки!", reply_markup=kb_menu_2)
# def end_walk(id):
#     try:
#         # Подключиться к существующей базе данных
#         conn = psycopg2.connect(
#             dbname='dog_shelter',
#             user='postgres',
#             password='Alex2001',
#             host='localhost')
#
#         cursor = conn.cursor()
#
#         current_date = date.today()
#         # print(current_date)
#
#         current_date_time = datetime.datetime.now()
#         current_time = current_date_time.time()
#         # print(current_time)
#
#         # Обновление отдельной записи
#         sql_update_query = """
#         Update walks set time_end = %s
#         where id = (SELECT w.id FROM walks as w
#         left join walks_members as wm ON w.id=wm.id
#         where wm.volonture_id = %s
#         order by w.id desc
#         limit 1)
#         """
#         cursor.execute(sql_update_query, (current_time, int(id)))
#         conn.commit()
#
#     except (Exception, Error) as error:
#         print("Ошибка при работе с PostgreSQL", error)
#     finally:
#         if conn:
#             cursor.close()
#             conn.close()
# @dp.message_handler(text="Завершить прогулку")
# async def end_walk_h(message: types.Message):
#
#     end_walk(message.from_user.id)
#     await message.answer(f"С возвращением!", reply_markup=kb_menu)
#
#
#



from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import admins
from handlers.utils.qr_code import read_qr
from aiogram import Bot, Dispatcher, executor, types

from Classifier.train import ResNet50_predict_breed, train_model
from keyboards.default import kb_menu
from keyboards.default.keyboard_menu import kb_menu_2
from loader import dp, bot
import pandas as pd
import psycopg2
import datetime
from datetime import date
from psycopg2 import Error
import warnings
warnings.simplefilter("ignore")

def add_walk(img, id):
    conn = psycopg2.connect(
        dbname='dog_shelter',
        user='postgres',
        password='Alex2001',
        host='localhost')

    cursor = conn.cursor()
    # Извлечение данных из таблицы
    sql_zap = '''SELECT * FROM walks'''
    zapros = pd.read_sql(sql_zap, conn)

    current_date = date.today()
    #print(current_date)

    current_date_time = datetime.datetime.now()
    current_time = current_date_time.time()
    #print(current_time)

    read_qr(img)
    cursor.execute('''INSERT INTO walks (id, date_of_walk, time_start, time_end, animal_id) 
        VALUES (%s, %s, %s, %s,%s)''',
                   (len(zapros), current_date, current_time, None, int(read_qr(img))))
    conn.commit()

    cursor.execute('''INSERT INTO walks_members (id, walk_id, worker_id, volonture_id) 
        VALUES (%s, %s, %s, %s)''',
                   (len(zapros), len(zapros), None, id))
    conn.commit()
    # Закрытие соединения
    cursor.close()
    conn.close()
# @dp.message_handler(text="Выйти на прогулку")
# async def create_walk(message: types.Message):
#     await message.answer(f"Пришлите QR-код собаки")
#     @dp.message_handler(content_types=[types.ContentType.PHOTO])
#     async def download_photo2(message: types.Message):
#         await message.photo[-1].download()
#         img_path = (await bot.get_file(message.photo[-1].file_id)).file_path
#         add_walk(img_path, message.from_user.id)
#         await message.answer(f"Хорошей прогулки!", reply_markup=kb_menu_2)
def end_walk(id):
    try:
        # Подключиться к существующей базе данных
        conn = psycopg2.connect(
            dbname='dog_shelter',
            user='postgres',
            password='Alex2001',
            host='localhost')

        cursor = conn.cursor()

        current_date = date.today()
        # print(current_date)

        current_date_time = datetime.datetime.now()
        current_time = current_date_time.time()
        # print(current_time)

        # Обновление отдельной записи
        sql_update_query = """
        Update walks set time_end = %s 
        where id = (SELECT w.id FROM walks as w
        left join walks_members as wm ON w.id=wm.id
        where wm.volonture_id = %s
        order by w.id desc
        limit 1) 
        """
        cursor.execute(sql_update_query, (current_time, int(id)))
        conn.commit()

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if conn:
            cursor.close()
            conn.close()
@dp.message_handler(text="Завершить прогулку")
async def end_walk_h(message: types.Message):

    end_walk(message.from_user.id)
    await message.answer(f"С возвращением!", reply_markup=kb_menu)


from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import admins
from handlers.utils.db_api import animals_t
from handlers.utils.db_api.query import animals_q
from handlers.utils.db_api.query.animals_q import insert_into_animals
#from keyboards.default import kb_test
#from keyboards.default.keyboard_tests import *

from loader import dp

from states.st_walks import state_walk



@dp.message_handler(text='Выйти на прогулку')
async def new_w(message: types.Message):
    await message.answer(f"Пришлите QR-код собаки")
    await state_walk.first()

# @dp.message_handler(text="Выйти на прогулку")
# async def create_walk(message: types.Message):
#     await message.answer(f"Пришлите QR-код собаки")
#     @dp.message_handler(content_types=[types.ContentType.PHOTO])
#     async def download_photo2(message: types.Message):
#         await message.photo[-1].download()
#         img_path = (await bot.get_file(message.photo[-1].file_id)).file_path
#         add_walk(img_path, message.from_user.id)
#         await message.answer(f"Хорошей прогулки!", reply_markup=kb_menu_2)
@dp.message_handler(state=state_walk.answer1,content_types=[types.ContentType.PHOTO])
async def state1(message: types.Message, state: FSMContext):
    await message.photo[-1].download()
    img_path = (await bot.get_file(message.photo[-1].file_id)).file_path
    add_walk(img_path, message.from_user.id)
    await message.answer(f"Хорошей прогулки!", reply_markup=kb_menu_2)
    await state.update_data(answer1 = img_path)
    data = await state.get_state()
    if data != None:
        await state.finish()


