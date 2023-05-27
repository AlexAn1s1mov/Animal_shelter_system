from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='База данных'),
            KeyboardButton(text='Календарь прогулок')
        ],
        [
            KeyboardButton(text='Определить породу собаки'),
            KeyboardButton(text='Выйти на прогулку')
        ],
    ],
    resize_keyboard=True
)

kb_menu_2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='База данных'),
            KeyboardButton(text='Календарь прогулок')
        ],
        [
            KeyboardButton(text='Определить породу собаки'),
            KeyboardButton(text='Завершить прогулку')
        ],
    ],
    resize_keyboard=True
)