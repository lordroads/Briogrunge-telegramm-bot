from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from database import questions

data_cb = CallbackData('Question', 'id', 'action')


def get_markup_client_menu() -> ReplyKeyboardMarkup:
    b1 = KeyboardButton('Вопросы')
    b2 = KeyboardButton('Вывоз_вещей')

    kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

    kb_client.add(b1).add(b2)

    return kb_client


def get_inline_questions_keyboard(action: str) -> InlineKeyboardMarkup:
    inline_markup = InlineKeyboardMarkup(row_width=1)

    for i, question in enumerate(questions.get_all()):
        number = i+1
        b_inline = InlineKeyboardButton(question, callback_data=data_cb.new(id=number, action=action))
        inline_markup.add(b_inline)

    return inline_markup
