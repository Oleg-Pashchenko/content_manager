import os

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
import random
import yandex_disk

TOKEN = os.getenv('TELEGRAM_TOKEN')

API_TOKEN = TOKEN

storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.reply(
        "Привет! Я бот, который умеет загружать фото, видео и кружочки.\nОтправь или перешли мне их и я загружу их на яндекс диск.\nТакже ты можешь добавить меня в группу (в том числе в обсуждение канала)!")


@dp.message_handler(content_types=['photo'])
async def handle_photos(message: types.Message):
    filename = f'{random.randint(1000000, 10000000)}.jpg'
    await message.photo[-1].download(filename)
    await yandex_disk.upload(filename)
    os.remove(filename)
    if message.chat.type == 'private':
        await message.reply("Фото загружено!")


@dp.message_handler(content_types=['video'])
async def handle_videos(message: types.Message):
    file_id = message.video.file_id
    file = await bot.get_file(file_id)
    filename = f'{random.randint(1000000, 10000000)}.mp4'
    await bot.download_file(file.file_path, filename)
    await yandex_disk.upload(filename)
    os.remove(filename)
    if message.chat.type == 'private':
        await message.reply("Видео загружено!")


@dp.message_handler(content_types=['video_note'])
async def handle_video_note(message: types.Message):
    file_id = message.video_note.file_id
    file = await bot.get_file(file_id)
    filename = f'{random.randint(1000000, 10000000)}.mp4'
    await bot.download_file(file.file_path, filename)
    await yandex_disk.upload(filename)
    os.remove(filename)
    if message.chat.type == 'private':
        await message.reply("Кружочек загружен!")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
