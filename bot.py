from aiogram import executor
import asyncio
from misc import dp
import handlers

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    executor.start_polling(dp, skip_updates=True)