from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='База данных'),
            KeyboardButton(text='Календарь прогулок')
        ],
        [
            KeyboardButton(text='Определить породу собаки')
        ],
        # [
        #     KeyboardButton(text='Помощь'),
        #     KeyboardButton(text='Контакты')
        # ]
    ],
    resize_keyboard=True
)