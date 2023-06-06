from asyncpg import UniqueViolationError

from handlers.utils.db_api.db_TelegramBot import db
from handlers.utils.db_api.schemas.user import Users


async def add_user(user_id: int, first_name: str, last_name: str, username: str, status: str):
    try:
        user = Users(user_id=user_id, first_name=first_name, last_name=last_name, username=username, status=status)
        await user.create()
    except UniqueViolationError:
        print('Пользователь не добавлен')


async def select_all_users():
    users = await Users.query.gino.all()
    return users


async def count_users():
    count = await db.func.count(Users.user_id).gino.scalar()
    return count


async def select_user(user_id):
    user = await Users.query.where(Users.user_id == user_id).gino.first()
    return user


async def update_status(user_id, status):
    user = await select_user(user_id)
    await user.update(status=status).apply()
