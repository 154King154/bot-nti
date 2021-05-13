from aiogram import types
from misc import dp, bot
import reply_texts as rt
from keyboards import keyboard_main_menu, keyboard_faq_1, keyboard_faq_2
from groups import BaseGroup, FAQGroup
from .general_commands import db


@dp.message_handler(state=FAQGroup.FAQ_1)
async def faq_1(message: types.Message):
    await message.answer(rt.faq_repeat, reply_markup=keyboard_faq_1)
    await FAQGroup.FAQ_1_ANSWER.set()


@dp.message_handler(state=FAQGroup.FAQ_1_ANSWER)
async def answer_faq_1(message: types.Message):
    if message.text == rt.faq_1:
        await message.answer(rt.faq_1_answer, parse_mode="HTML", reply_markup=keyboard_faq_1)
    elif message.text == rt.faq_2:
        await message.answer(rt.faq_2_answer, parse_mode="HTML", reply_markup=keyboard_faq_1)
    elif message.text == rt.faq_3:
        await message.answer(rt.faq_3_answer, parse_mode="HTML", reply_markup=keyboard_faq_1)
    elif message.text == rt.faq_4:
        await message.answer(rt.faq_4_answer, parse_mode="HTML", reply_markup=keyboard_faq_1)
    elif message.text == rt.faq_5:
        await message.answer(rt.faq_5_answer, parse_mode="HTML", reply_markup=keyboard_faq_1)
    elif message.text == rt.faq_6:
        await message.answer(rt.faq_6_answer, parse_mode="HTML", reply_markup=keyboard_faq_1)
    elif message.text == rt.faq_7:
        await message.answer(rt.faq_7_answer, parse_mode="HTML", reply_markup=keyboard_faq_1)
    elif message.text == rt.faq_8:
        await message.answer(rt.faq_8_answer, parse_mode="HTML", reply_markup=keyboard_faq_1)
    elif message.text == rt.faq_9:
        await message.answer(rt.faq_9_answer, parse_mode="HTML", reply_markup=keyboard_faq_1)
    elif message.text == rt.faq_10:
        await message.answer(rt.faq_10_answer, parse_mode="HTML", reply_markup=keyboard_faq_1)
    elif message.text == rt.faq_11:
        await message.answer(rt.faq_11_answer, parse_mode="HTML", reply_markup=keyboard_faq_1)
    elif message.text == rt.faq_22:
        await message.answer(rt.faq_22_answer, parse_mode="HTML", reply_markup=keyboard_faq_1)
    elif message.text == rt.faq_23:
        await message.answer(rt.faq_23_answer, parse_mode="HTML", reply_markup=keyboard_faq_1)
    elif message.text == 'Далее':
        await message.answer(rt.faq_next_page, parse_mode="HTML", reply_markup=keyboard_faq_2)
        await FAQGroup.FAQ_2_ANSWER.set()


@dp.message_handler(state=FAQGroup.FAQ_2_ANSWER)
async def answer_faq_2(message: types.Message):
    if message.text == rt.faq_12:
        await message.answer(rt.faq_12_answer, parse_mode="HTML", reply_markup=keyboard_faq_2)
    elif message.text == rt.faq_13:
        await message.answer(rt.faq_13_answer, parse_mode="HTML", reply_markup=keyboard_faq_2)
    elif message.text == rt.faq_15:
        await message.answer(rt.faq_15_answer, parse_mode="HTML", reply_markup=keyboard_faq_2)
    elif message.text == rt.faq_16:
        await message.answer(rt.faq_16_answer, parse_mode="HTML", reply_markup=keyboard_faq_2)
    elif message.text == rt.faq_17:
        await message.answer(rt.faq_17_answer,parse_mode="HTML", reply_markup=keyboard_faq_2)
    elif message.text == rt.faq_18:
        await message.answer(rt.faq_18_answer, parse_mode="HTML", reply_markup=keyboard_faq_2)
    elif message.text == rt.faq_19:
        await message.answer(rt.faq_19_answer, parse_mode="HTML", reply_markup=keyboard_faq_2)
    elif message.text == rt.faq_20:
        await message.answer(rt.faq_20_answer, parse_mode="HTML", reply_markup=keyboard_faq_2)
    elif message.text == rt.faq_21:
        await message.answer(rt.faq_21_answer, parse_mode="HTML", reply_markup=keyboard_faq_2)
    elif message.text == 'В начало':
        await BaseGroup.S_MAIN_MENU.set()
        await message.answer(rt.choice_menu, parse_mode="HTML", reply_markup=keyboard_main_menu)
