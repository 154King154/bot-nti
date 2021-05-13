import reply_texts as rt
from aiogram import types

keyboard_continue = types.ReplyKeyboardMarkup(True, True)
keyboard_continue.row('Продолжить')

keyboard_main_menu = types.ReplyKeyboardMarkup(True, True)
keyboard_main_menu.row("FAQ", "Задать вопрос")

list_faq_1 = [rt.faq_1, rt.faq_2, rt.faq_3, rt.faq_4, rt.faq_5, rt.faq_6,
              rt.faq_7, rt.faq_8, rt.faq_9, rt.faq_10, rt.faq_11, 'Далее']
list_faq_2 = [rt.faq_12, rt.faq_13, rt.faq_16, rt.faq_17,
              rt.faq_18, rt.faq_19, rt.faq_20, rt.faq_21, 'В начало']

keyboard_faq_1 = types.ReplyKeyboardMarkup(True, True)
keyboard_faq_1.row(rt.faq_1, rt.faq_22)
keyboard_faq_1.row(rt.faq_2, rt.faq_23)
keyboard_faq_1.row(rt.faq_3)
keyboard_faq_1.row(rt.faq_4)
keyboard_faq_1.row(rt.faq_5)
keyboard_faq_1.row(rt.faq_6)
keyboard_faq_1.row(rt.faq_7)
keyboard_faq_1.row(rt.faq_8)
keyboard_faq_1.row(rt.faq_9)
keyboard_faq_1.row(rt.faq_10)
keyboard_faq_1.row(rt.faq_11)
keyboard_faq_1.row('Далее')

keyboard_faq_2 = types.ReplyKeyboardMarkup(True, True)
for que in list_faq_2:
    keyboard_faq_2.row(que)

keyboard_to_main = types.ReplyKeyboardMarkup(True, True)
keyboard_to_main.row('В главное меню')

keyboard_confirm = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard_confirm.row("Все верно")
keyboard_confirm.row("Пройти регистрацию заново")

keyboard_delete_main = types.ReplyKeyboardMarkup(True, True)
keyboard_delete_main.row("Да", "Нет")

keyboard_company = types.ReplyKeyboardMarkup(True, True)
keyboard_company.row("Университет 2035", "Платформа НТИ")