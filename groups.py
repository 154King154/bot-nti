from aiogram.dispatcher.filters.state import State, StatesGroup


class FAQGroup(StatesGroup):
    FAQ_1 = State()
    FAQ_1_ANSWER = State()
    FAQ_2 = State()
    FAQ_2_ANSWER = State()


class HelpGroup(StatesGroup):
    HELP = State()
    ANSWER = State()
    ANSWER_SEND = State()


class BaseGroup(StatesGroup):
    S_RESTART = State()
    S_MAIN_MENU = State()


class Registration(StatesGroup):
    R_NAME = State()
    R_COMPANY = State()
    R_DEPARTMENT = State()
    R_MAIL = State()
    R_CONFIRM = State()
    R_END = State()
    R_NEW = State()