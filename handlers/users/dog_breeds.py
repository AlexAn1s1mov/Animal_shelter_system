from aiogram import Bot, Dispatcher, executor, types

from Classifier.train import ResNet50_predict_breed, train_model
from keyboards.default import kb_menu
from loader import dp, bot


@dp.message_handler(text='Определить породу собаки')
async def classify_breed(message: types.Message):
    await message.answer(f"Отправьте фото собаки")
    @dp.message_handler(content_types=[types.ContentType.PHOTO])
    async def download_photo(message: types.Message):
    # загружаем фото в папку по умолчанию
       await message.photo[-1].download()
    # определяем путь к фото
       img_path = (await bot.get_file(message.photo[-1].file_id)).file_path
    # получаем предсказание
       await message.answer(f"Определяем породу собаки...")
       pred = ResNet50_predict_breed(img_path)

       await message.answer(f"{pred}")