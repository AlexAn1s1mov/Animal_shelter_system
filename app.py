import asyncio

from Classifier.train import train_model
from handlers.users.notification import scheduler


async def on_startup(dp):

    from loader import db
    from handlers.utils.db_api.db_TelegramBot import on_startup
    print('Подключение к PostgreSQL')
    await on_startup(dp)

    print('Создание таблиц')
    await db.gino.create_all()
    print('Готово')

    from handlers.utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)

    from handlers.utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)

    asyncio.create_task(scheduler())

    print('Bot activated')

    train_model()
    print('Model is ready')

if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
