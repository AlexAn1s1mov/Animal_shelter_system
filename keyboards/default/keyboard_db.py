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

kb_db_tools = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Добавить'),
            KeyboardButton(text='Изменить'),
        ],
        [
            KeyboardButton(text='Удалить'),
            KeyboardButton(text='Просмотреть')
        ],
        [
            KeyboardButton(text='Главное меню')
        ]
    ],
    resize_keyboard=True
)