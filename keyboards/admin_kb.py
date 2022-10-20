from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from database import questions


def get_markup_admin_menu() -> ReplyKeyboardMarkup:
    b1 = KeyboardButton('Вопросы')
    b2 = KeyboardButton('Вывоз_вещей')
    b3 = KeyboardButton('Добавить вопрос')
    b4 = KeyboardButton('Удалить вопрос')
    b5 = KeyboardButton('Редактировать вопрос')
    b6 = KeyboardButton('Отмена')
    b7 = KeyboardButton('Редактировать пользователя')

    kb_admin = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    kb_admin.add(b1).add(b2).row(b3, b4, b5, b6).row(b7)

    return kb_admin
