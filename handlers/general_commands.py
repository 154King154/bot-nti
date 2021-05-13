from aiogram import types
from groups import BaseGroup, HelpGroup, Registration
from misc import dp, bot, db
import reply_texts as rt
from keyboards import keyboard_main_menu
from asyncpg import Connection, Record
from asyncpg.exceptions import UniqueViolationError
import datetime as dt
import config


class DBCommands:
    pool: Connection = db
    ADD_USER_ID = "INSERT INTO lama_users(chat_id) " \
                  "VALUES ($1);"
    ADD_NEW_ACT = "INSERT INTO lama_logs(chat_id, date, time, type, context) " \
                  "VALUES ($1, $2, $3, $4, $5);"
    ADD_USER = "INSERT INTO users(chat_id, date, time, username, nickname, department, company) " \
               "VALUES ($1, $2, $3, $4, $5, $6, $7);"
    COUNT_ACTS = "SELECT COUNT(*) FROM lama_logs"
    CHECK_USER = "SELECT COUNT(*) FROM lama_users WHERE chat_id={}"
    CHECK_REG_USER = "SELECT COUNT(*) FROM users WHERE chat_id={}"
    COUNT_USERS = "SELECT COUNT(DISTINCT chat_id) FROM lama_logs"
    GET_IDS = "SELECT DISTINCT chat_id FROM lama_logs"

    async def add_user_id(self, chat_id):
        args = [chat_id]
        command = self.ADD_USER_ID

        try:
            _ = await self.pool.fetch(command, *args)
        except UniqueViolationError:
            pass

    async def add_new_user(self, chat_id, username, nickname, department, company):
        date = dt.datetime.now().strftime("%Y-%m-%d")
        time = dt.datetime.now().strftime("%H:%M:%S")
        args = chat_id, date, time, username, nickname, department, company
        command = self.ADD_USER

        try:
            _ = await self.pool.fetch(command, *args)
        except UniqueViolationError:
            pass

    async def add_new_act(self, chat_id, type, context):
        args = chat_id, dt.datetime.now().strftime("%Y-%m-%d"), dt.datetime.now().strftime("%H:%M:%S"), \
               type, context
        command = self.ADD_NEW_ACT

        try:
            _ = await self.pool.fetch(command, *args)
        except UniqueViolationError:
            pass

    async def count_acts(self):
        record: Record = await self.pool.fetchval(self.COUNT_ACTS)
        return record

    async def check_user(self, chat_id):
        command = self.CHECK_USER

        try:
            record = await self.pool.fetchval(command.format(chat_id))
            return record
        except UniqueViolationError:
            return "error"

    async def check_user_reg(self, chat_id):
        command = self.CHECK_REG_USER

        try:
            record = await self.pool.fetchval(command.format(chat_id))
            return record
        except UniqueViolationError:
            return "error"

    async def get_users_id(self):
        record: Record = await self.pool.fetch(self.GET_IDS)
        return record


db = DBCommands()


@dp.message_handler(commands="start", state="*")
async def start(message: types.Message):
    if await db.check_user_reg(chat_id=message.chat.id) > 0:
        if await db.check_user(chat_id=message.chat.id) <= 0:
            await db.add_user_id(message.chat.id)

        await message.answer(rt.welcome_message, reply_markup=keyboard_main_menu)
        await message.answer_sticker("CAACAgIAAxkBAAL9QV77Kt0h2xrqEbXjT95IrWgyijwDAAJvAAOcDygJpNyi5T1jtbIaBA")
        # await message.answer("Id чата: {}".format(message.chat.id))
        await BaseGroup.S_MAIN_MENU.set()
    else:
        await message.answer(rt.start_welcome_message)
        await message.answer(rt.reg_start)
        await Registration.R_NAME.set()


@dp.message_handler(commands="reply", state="*")
async def help_command(message: types.Message):
    if message.chat.id == config.team_id:
        await message.answer(rt.help_procedure)
        await HelpGroup.ANSWER.set()


@dp.message_handler(commands="send_all", state="*")
async def send_all_command(message: types.Message):
    if message.chat.id == config.team_id:
        await message.answer(rt.send_procedure)
        await HelpGroup.ANSWER_SEND.set()

'''
@dp.message_handler(commands="get_stats", state="*")
async def get_stats(message: types.Message):
    acts = await db.count_acts()
    users = await db.count_users()
    faqs = await db.count_faqs()
    docs = await db.count_docs()
    users_a_start = await db.count_ada_start()
    users_a_end = await db.count_ada_end()
    quiz_count = await db.count_quiz_users()
    quiz = await db.count_quiz()
    quiz_avg = await db.quiz_avg()
    await message.answer(rt.stats_message.format(acts=acts, users=users, faqs=faqs, docs=docs,
                                                 users_a_start=users_a_start, users_a_end=users_a_end,
                                                 quiz_count=quiz_count, quiz=quiz, quiz_avg=quiz_avg),
                         reply_markup=keyboard_main_menu)
    # await message.answer("Id чата: {}".format(message.chat.id))
    await BaseGroup.S_MAIN_MENU.set()
    await db.add_new_act(chat_id=message.chat.id, state_global='get_stats', state_in_block='get_stats')
'''