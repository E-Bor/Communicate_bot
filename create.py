from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, storage
from config import TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from database.database import UserData

"""file for error avoidance in class Bot, dispatcher"""

storage = MemoryStorage()
bot = Bot(token=TOKEN,parse_mode="MarkdownV2")
dp = Dispatcher(bot, storage=storage)
database = UserData()
