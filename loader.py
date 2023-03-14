from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils import config

bot = Bot(token=config.config("5960016521:AAGks9H2W8pWlYKowUD93rGj8-xz11YwBXI"), parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
vip = Dispatcher(bot, storage=storage)
