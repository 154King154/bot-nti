from aiogram import types
from misc import dp, bot
import config
import reply_texts as rt
from groups import BaseGroup, HelpGroup
from keyboards import keyboard_continue, keyboard_main_menu
from .general_commands import db


@dp.message_handler(state=HelpGroup.HELP)
async def help_start(message: types.Message):
    if message.text == "Отмена":
        await message.answer_sticker('CAACAgIAAxkBAAL3Z17xvSAfCN9gmMCLJZjDb9eE22U6AAJ4AAOcDygJ4Sfz8nF5fR8aBA',
                                     reply_markup=keyboard_main_menu)
        await BaseGroup.S_MAIN_MENU.set()
    else:
        await message.answer(rt.help_wait, parse_mode="HTML", reply_markup=keyboard_main_menu)
        await bot.send_message(config.team_id, rt.help_start_answer.format(message.chat.id))
        await message.forward(config.team_id)
        await BaseGroup.S_MAIN_MENU.set()


@dp.message_handler(state=HelpGroup.ANSWER)
async def help_answer(message: types.Message):
    string = message.text.split(" ")
    await bot.send_message(string[0], rt.question_answer.format(answer=' '.join(string[1:])))
    await message.answer("Сообщение доставлено")
    await BaseGroup.S_MAIN_MENU.set()


@dp.message_handler(state=HelpGroup.ANSWER_SEND)
async def send_all_answer(message: types.Message):
    sended_mess = message.text
    users_id = await db.get_users_id()
    for ID in users_id:
        ID_prep = str(ID)[16:-1]
        try:
            await bot.send_message(int(ID_prep), sended_mess)
            print("message sended", ID_prep)
        except:
            print("No chat for user")
            continue
    await bot.send_message(config.team_id, "Рассылка выполнена")
    await BaseGroup.S_MAIN_MENU.set()
