from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_db = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Работа с базой данных'),
            KeyboardButton(text='Получить информацию')
        ],
        [
            KeyboardButton(text='Главное меню')
        ]
    ],
    resize_keyboard=True
)

kb_db_admin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Пользователи'),
            KeyboardButton(text='Роли'),
            KeyboardButton(text='Вольеры')
        ],
        [
            KeyboardButton(text='Типы'),
            KeyboardButton(text='Животные'),
            KeyboardButton(text='Вакцины')
        ],
        [
            KeyboardButton(text='Пользователи'),
            KeyboardButton(text='Прогулки'),
            KeyboardButton(text='Участники прогулки')
        ],
        [
            KeyboardButton(text='Главное меню')
        ]
    ],
    resize_keyboard=True
)

kb_db_tools_animal = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Добавить животное'),
            KeyboardButton(text='Изменить животное'),
        ],
        [
            KeyboardButton(text='Удалить животное'),
            KeyboardButton(text='Просмотреть')
        ],
        [
            KeyboardButton(text='Главное меню')
        ]
    ],
    resize_keyboard=True
)

kb_db_calendar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Прогулки за сегодня'),
            KeyboardButton(text='Прогулки за неделю'),
            KeyboardButton(text='Прогулки за месяц'),
        ],
        [
            KeyboardButton(text='Главное меню')
        ]
    ],
    resize_keyboard=True
)

kb_db_query = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='О животном'),
            KeyboardButton(text='Количество собак в приюте'),



        ],
        [
            KeyboardButton(text='Главное меню')
        ]
    ],
    resize_keyboard=True
)
