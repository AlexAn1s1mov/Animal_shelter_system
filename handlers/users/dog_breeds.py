from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext

from Classifier.train import ResNet50_predict_breed, train_model
from keyboards.default import kb_menu
from loader import dp, bot
from states.st_dog_photo import state_dog


#img_path = ''
# @dp.message_handler(text='Определить породу собаки')
# async def classify_breed(message: types.Message):
#     await message.answer(f"Отправьте фото собаки")
#     @dp.message_handler(content_types=[types.ContentType.PHOTO])
#     async def download_photo(message: types.Message):
#     # загружаем фото в папку по умолчанию
#         await message.photo[-1].download()
#     # определяем путь к фото
#         global img_path
#         img_path = (await bot.get_file(message.photo[-1].file_id)).file_path
#     # получаем предсказание
#     await message.answer(f"Определяем породу собаки...")
#     pred = ResNet50_predict_breed(img_path)
#
#     await message.answer(f"{pred}")

@dp.message_handler(text='Определить породу собаки')
async def classify_breed(message: types.Message):
    await message.answer(f"Отправьте фото собаки")
    await state_dog.first()
@dp.message_handler(state=state_dog.answer1,content_types=[types.ContentType.PHOTO])
async def state1(message: types.Message, state: FSMContext):
    await message.photo[-1].download()
    img_path = (await bot.get_file(message.photo[-1].file_id)).file_path
    await message.answer(f"Определяем породу собаки...")
    pred = ResNet50_predict_breed(img_path)

    await message.answer(f"{pred}")
    await state.update_data(answer1 = img_path)
    data = await state.get_state()
    if data != None:
        await state.finish()
# @dp.message_handler(text='Определить породу собаки')
# async def classify_breed(message: types.Message):
#     await message.answer(f"Отправьте фото собаки")
#     @dp.message_handler(content_types=[types.ContentType.PHOTO])
#     async def download_photo(message: types.Message):
#     # загружаем фото в папку по умолчанию
#        await message.photo[-1].download()
#     # определяем путь к фото
#        img_path = (await bot.get_file(message.photo[-1].file_id)).file_path
#     # получаем предсказание
#        await message.answer(f"Определяем породу собаки...")
#        pred = ResNet50_predict_breed(img_path)
#
#        await message.answer(f"{pred}")