from aiogram import Bot, types, executor, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

TOKEN = 'TOKEN'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage = MemoryStorage())


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await message.reply('Assalomu alaykum! Men X do`koni fayl qabul qiluvchi botman.\nЗдравствуйте! Я бот-приёмник файлов магазина X.')

@dp.message_handler(content_types=['document','file'])
async def get_file(message: types.Message):
    file_id = message.document.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    await bot.download_file(file_path=file_path, destination=f"downloads\{message.document.file_name}")
    await message.reply('Qabul qilindi.\n Принято.')

if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)