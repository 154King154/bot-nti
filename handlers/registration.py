from aiogram import types
from misc import dp, bot
import reply_texts as rt
from groups import *
from keyboards import *
from aiogram.dispatcher import FSMContext
from .general_commands import db
from .adaptation import adaptation_loop


@dp.message_handler(state=Registration.R_NAME)
async def reg_name(message: types.Message, state: FSMContext):
    username = message.text
    await state.update_data(username=username)
    await message.answer(rt.reg_company, reply_markup=keyboard_company)
    await Registration.R_COMPANY.set()


@dp.message_handler(state=Registration.R_COMPANY)
async def reg_company(message: types.Message, state: FSMContext):
    user_company = message.text
    await state.update_data(user_company=user_company)
    await message.answer(rt.reg_department)
    await Registration.R_DEPARTMENT.set()


@dp.message_handler(state=Registration.R_DEPARTMENT)
async def reg_department(message: types.Message, state: FSMContext):
    user_department = message.text
    await state.update_data(user_department=user_department)
    user_data = await state.get_data()
    await message.answer(rt.reg_confirm)
    await message.answer(rt.user_form.format(username=user_data['username'],
                                             department=user_data['user_department'],
                                             company=user_data['user_company'],
                                             nickname=message.chat.username),
                         reply_markup=keyboard_confirm)
    await Registration.R_END.set()


@dp.message_handler(state=Registration.R_END)
async def reg_confirm(message: types.Message, state: FSMContext):
    if message.text == "Все верно":
        user_data = await state.get_data()
        check = await db.check_user(message.chat.id)
        if check > 0:
            await db.remove_user(chat_id=message.chat.id)

        await db.add_new_user(chat_id=message.chat.id, username=user_data['username'],
                              nickname=message.chat.username, company=user_data['user_company'],
                              department=user_data['user_department'])
        await db.add_user_id(message.chat.id)

        await message.answer(rt.reg_new, reply_markup=keyboard_delete_main)
        await Registration.R_NEW.set()

    elif message.text == "Пройти регистрацию заново":
        await message.answer(rt.reg_name)
        await Registration.R_NAME.set()


@dp.message_handler(state=Registration.R_NEW)
async def reg_new(message: types.Message, state: FSMContext):
    if message.text == "Да":
        await message.answer(rt.main_message, reply_markup=keyboard_main_menu)
        await BaseGroup.S_MAIN_MENU.set()
        await adaptation_loop(message.chat.id)
    else:
        await message.answer(rt.main_message, reply_markup=keyboard_main_menu)
        await BaseGroup.S_MAIN_MENU.set()


