import logging
import asyncio
from token_telegram import token
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import *
from sql import create_pool

bot = Bot(token)
storage = RedisStorage2(db=1)
dp = Dispatcher(bot, storage=storage)
db = dp.loop.run_until_complete(create_pool())
logging.basicConfig(level=logging.INFO)
