#
# from aiogram import types
# from aiogram.dispatcher import FSMContext
#
# from data.config import admins
# from handlers.utils.db_api import animals_t
# from keyboards.default import kb_test
# from keyboards.default.keyboard_tests import *
#
# from loader import dp
#
# from states.animals_states import animals_new
#
#
#
# # @dp.message_handler(text='Добавить', state='*')
# # async def test1_answers_end(message: types.Message):
# #     await message.answer(f'Вы уверены?', reply_markup=ReplyKeyboardMarkup(
# #     keyboard=[
# #         [
# #             KeyboardButton(text='Прервать тест на канал восприятия')
# #         ],
# #         [
# #             KeyboardButton(text='Продолжить тест на канал восприятия')
# #         ]
# #     ],
# #     resize_keyboard=True
# # ))
#
# @dp.message_handler(text='Добавить')
# async def add_animal(message: types.Message):
#     if message.from_user.id in admins:
#         global cur_table
#         if cur_table == 'Животные':
#             await message.answer(f'Введите тип животного: ')
#             await animals_new.first()
#
# @dp.message_handler(state=animals_new.answer1)
# async def state1(message: types.Message, state: FSMContext):
#     answer = message.text.lower()
#     await state.update_data(answer1 = answer)
#     await message.answer(f'Введите имя животного: ')
#     data = await state.get_state()
#     if data != None:
#         await animals_new.next()
#
# @dp.message_handler(state=animals_new.answer2)
# async def state2(message: types.Message, state: FSMContext):
#     answer = message.text.lower()
#     await state.update_data(answer2 = answer)
#     await message.answer(f'Введите возраст животного: ')
#     data = await state.get_state()
#     if data != None:
#         await animals_new.next()
#
# @dp.message_handler(state=animals_new.answer3)
# async def state3(message: types.Message, state: FSMContext):
#     answer = message.text.lower()
#     await state.update_data(answer3 = answer)
#     await message.answer(f'Введите дату поступления в приют животного: ')
#     data = await state.get_state()
#     if data != None:
#         await animals_new.next()
#
# @dp.message_handler(state=animals_new.answer4)
# async def state4(message: types.Message, state: FSMContext):
#     answer = message.text.lower()
#     await state.update_data(answer4 = answer)
#     await message.answer(f'Введите дату выпуска из приюта животного (если есть): ')
#     data = await state.get_state()
#     if data != None:
#         await animals_new.next()
#
# @dp.message_handler(state=animals_new.answer5)
# async def state5(message: types.Message, state: FSMContext):
#     answer = message.text.lower()
#     await state.update_data(answer5 = answer)
#     await message.answer(f'Введите статус животного \n'
#                          f'(находится в приюте, передан в новый дом, усыплен): ')
#     data = await state.get_state()
#     if data != None:
#         await animals_new.next()
#
# @dp.message_handler(state=animals_new.answer6)
# async def state6(message: types.Message, state: FSMContext):
#     answer = message.text.lower()
#     await state.update_data(answer6 = answer)
#     await message.answer(f'Введите номер вольера: ')
#     data = await state.get_state()
#     if data != None:
#         await animals_new.next()
#
# @dp.message_handler(state=animals_new.answer7)
# async def state7(message: types.Message, state: FSMContext):
#     answer = message.text.lower()
#     await state.update_data(answer7 = answer)
#     data = await state.get_data()
#     list = []
#     for i in range(len(data)):
#         string = 'answer' + f'{i + 1}'
#         list.append(data[string])
#
#     id_ = message.from_user.id + 1
#     await animals_t.new_animal(id=id_,
#                                    user_id=message.from_user.id,
#                                    test_number=name,
#                                    test_name=about_tests[name]["name"],
#                                    results=test1_score(list),
#                                    status='created')
#     await animals_t.update_result(id=id_, results=test1_score(list))
#
#     await message.answer(f'{test1_score(list)}', reply_markup=kb_test)
#     data = await state.get_state()
#     if data != None:
#         cnt = 0
#         await state.finish()
#
