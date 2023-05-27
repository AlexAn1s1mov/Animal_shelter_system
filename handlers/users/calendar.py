from aiogram import types

from data.config import admins
from handlers.utils.db_api.query.animals_q import *
from loader import dp
from keyboards.default import *

@dp.message_handler(text='Календарь прогулок')
async def calendar(message: types.Message):
    await message.answer(f'Выберите временной промежуток', reply_markup=kb_db_calendar)

@dp.message_handler(text='Прогулки за сегодня')
async def walks_today(message: types.Message):
    conn = psycopg2.connect(
        dbname='dog_shelter',
        user='postgres',
        password='Alex2001',
        host='localhost')

    # Извлечение данных из таблицы
    sql_zap = '''Select w.time_start,w.time_end, a.name, u.first_name, u.last_name from
    walks as w left join walks_members as wm on w.id=wm.id
    left join animals as a on w.animal_id=a.id
    left join users as u on wm.volonture_id=u.user_id
    where w.date_of_walk=current_date 
        '''
    zapros = pd.read_sql(sql_zap, conn)

    # Вывод данных на экран
    print(zapros)
    # Закрытие соединения
    conn.close()
    await message.answer(f'Результат:\n'
                         f' {zapros}!')

@dp.message_handler(text='Прогулки за неделю')
async def walks_today(message: types.Message):
    conn = psycopg2.connect(
        dbname='dog_shelter',
        user='postgres',
        password='Alex2001',
        host='localhost')

    # Извлечение данных из таблицы
    sql_zap = '''Select w.time_start,w.time_end, a.name, u.first_name, u.last_name from
    walks as w left join walks_members as wm on w.id=wm.id
    left join animals as a on w.animal_id=a.id
    left join users as u on wm.volonture_id=u.user_id
    where w.date_of_walk>current_date-6
        '''
    zapros = pd.read_sql(sql_zap, conn)

    # Вывод данных на экран
    print(zapros)
    # Закрытие соединения
    conn.close()
    await message.answer(f'Результат:\n'
                         f' {zapros}!')

@dp.message_handler(text='Прогулки за месяц')
async def walks_today(message: types.Message):
    conn = psycopg2.connect(
        dbname='dog_shelter',
        user='postgres',
        password='Alex2001',
        host='localhost')

    # Извлечение данных из таблицы
    sql_zap = '''Select w.time_start,w.time_end, a.name, u.first_name, u.last_name from
    walks as w left join walks_members as wm on w.id=wm.id
    left join animals as a on w.animal_id=a.id
    left join users as u on wm.volonture_id=u.user_id
    where w.date_of_walk>current_date-6
        '''
    zapros = pd.read_sql(sql_zap, conn)

    # Вывод данных на экран
    print(zapros)
    # Закрытие соединения
    conn.close()
    await message.answer(f'Результат:\n'
                         f' {zapros}!')

def walks_today():
    conn = psycopg2.connect(
        dbname='dog_shelter',
        user='postgres',
        password='Alex2001',
        host='localhost')

    # Извлечение данных из таблицы
    sql_zap = '''Select w.time_start,w.time_end, a.name, u.first_name, u.last_name from
walks as w left join walks_members as wm on w.id=wm.id
left join animals as a on w.animal_id=a.id
left join users as u on wm.volonture_id=u.user_id
where w.date_of_walk=current_date 
    '''
    zapros = pd.read_sql(sql_zap, conn)

    # Вывод данных на экран
    print(zapros)
    # Закрытие соединения
    conn.close()