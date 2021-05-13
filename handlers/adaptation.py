from misc import bot, dp
import logging
import datetime as dt
import pandas as pd
import random
import asyncio
import adaptation_texts as at
from aiogram.utils import executor


async def wait_until(date):
    # sleep until the specified datetime
    now = dt.datetime.now()
    await asyncio.sleep((date - now).total_seconds())


async def adaptation_loop(chat_id):
    await bot.send_message(chat_id, at.ada_1, parse_mode="HTML")
    date = dt.datetime.now() + dt.timedelta(hours=1)
    await wait_until(date)

    await bot.send_message(chat_id, at.ada_2, parse_mode="HTML")
    date = dt.datetime.now() + dt.timedelta(hours=23)
    await wait_until(date)

    await bot.send_message(chat_id, at.ada_3, parse_mode="HTML")
    date = dt.datetime.now() + dt.timedelta(hours=1)
    await wait_until(date)

    await bot.send_message(chat_id, at.ada_4, parse_mode="HTML")
    date = dt.datetime.now() + dt.timedelta(hours=23)
    await wait_until(date)

    await bot.send_message(chat_id, at.ada_5, parse_mode="HTML")
    date = dt.datetime.now() + dt.timedelta(hours=1)
    await wait_until(date)

    await bot.send_message(chat_id, at.ada_6, parse_mode="HTML")
    date = dt.datetime.now() + dt.timedelta(hours=23)
    await wait_until(date)
