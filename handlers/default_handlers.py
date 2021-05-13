from aiogram import types
from misc import dp, bot
import reply_texts as rt
from groups import *
from keyboards import *
from aiogram.dispatcher import FSMContext
from .general_commands import db


@dp.message_handler(state=BaseGroup.S_MAIN_MENU)
async def main_menu(message: types.Message, state: FSMContext):
    if message.text == 'FAQ':
        await message.answer(rt.faq_welcome, reply_markup=keyboard_faq_1)
        await FAQGroup.FAQ_1_ANSWER.set()
    elif message.text == "Задать вопрос":
        keyboard = types.ReplyKeyboardMarkup(True, True)
        keyboard.row('Отмена')
        await message.answer(rt.help_welcome, reply_markup=keyboard)
        await HelpGroup.HELP.set()
