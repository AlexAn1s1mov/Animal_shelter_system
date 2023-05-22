from asyncpg import UniqueViolationError

from handlers.utils.db_api.schemas.animals import Animals


async def new_animal(kind: str, name: str, age: int, date_of_enter: str, date_of_exit: str, status: str, Enclosure_id: int):
    try:
        animals = Animals(kind = kind, name = name, age = age, date_of_enter = date_of_enter, date_of_exit = date_of_exit, status = status, Enclosure_id = Enclosure_id)
        await animals.create()
    except UniqueViolationError:
        print('Результат не добавлен или обновлён')

# async def select_result():
#     result = await Results.query.where(Results.status == 'created').gino.first()
#     return result
#
# async def select_result_by_user_id(id: int):
#     result = await Results.query.where(Results.id == id).gino.first()
#     return result
#
# async def update_result(id, results):
#     result = await select_result_by_user_id(id)
#     await result.update(results=results).apply()