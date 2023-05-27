import pandas as pd
import psycopg2
from psycopg2 import Error
import warnings
warnings.simplefilter("ignore")
from handlers.utils.qr_code import *

import psycopg2
import pandas as pd


def select_all_animals():
    try:
        # Подключение к базе данных
        conn = psycopg2.connect(
            dbname='dog_shelter',
            user='postgres',
            password='Alex2001',
            host='localhost')

        # Извлечение данных из таблицы
        sql_zap = '''SELECT * FROM animals'''
        zapros = pd.read_sql(sql_zap, conn)

        # Закрытие соединения
        conn.close()
        # Закрытие соединения
        return (zapros)

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if conn:
            conn.close()


def insert_into_animals(kind, name, sex, date_of_birth, chip, date_of_enter, date_of_exit, status, enclosure_id):
    try:
        conn = psycopg2.connect(
            dbname='dog_shelter',
            user='postgres',
            password='Alex2001',
            host='localhost')

        cursor = conn.cursor()
        # Извлечение данных из таблицы
        sql_zap = '''SELECT * FROM animals'''
        zapros = pd.read_sql(sql_zap, conn)

        from handlers.utils.qr_code import create_qr
        qr_path = str(create_qr(str(len(zapros))))

        cursor.execute('''INSERT INTO animals (id, kind, name, sex, date_of_birth, chip,
            date_of_enter, date_of_exit, status, enclosure_id, qr_path) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                       (len(zapros), kind, name, sex, date_of_birth, chip, date_of_enter, date_of_exit, status,
                        enclosure_id, qr_path))
        conn.commit()
        # Закрытие соединения
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if conn:
            cursor.close()
            conn.close()


def update_animals(id, type):
    try:
        # Подключиться к существующей базе данных
        conn = psycopg2.connect(
            dbname='dog_shelter',
            user='postgres',
            password='Alex2001',
            host='localhost')

        cursor = conn.cursor()

        # Обновление отдельной записи
        sql_update_query = """Update animals set enclosure_id = %s where id = %s"""
        cursor.execute(sql_update_query, (type, id))
        conn.commit()

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if conn:
            cursor.close()
            conn.close()


def delet_animals(id):
    try:
        # Подключиться к существующей базе данных
        conn = psycopg2.connect(
            dbname='dog_shelter',
            user='postgres',
            password='Alex2001',
            host='localhost')

        cursor = conn.cursor()

        sql_delete_query = """Delete from animals where id = %s"""
        cursor.execute(sql_delete_query, (id,))
        conn.commit()

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if conn:
            cursor.close()
            conn.close()


def id_animal_select(id):
    try:
        # Подключение к базе данных
        conn = psycopg2.connect(
            dbname='dog_shelter',
            user='postgres',
            password='Alex2001',
            host='localhost')

        # Извлечение данных из таблицы
        sql_zap = '''SELECT * FROM animals
        where id = {}'''.format(id)
        zapros = pd.read_sql(sql_zap, conn)

        # Закрытие соединения
        conn.close()
        # Закрытие соединения
        return (zapros)

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if conn:
            conn.close()