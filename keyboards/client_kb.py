from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from database import questions

data_cb = CallbackData('Question', 'id', 'action')

b1 = KeyboardButton('Вопросы')
b2 = KeyboardButton('Вывоз_вещей')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b1).add(b2)


def get_inline_questions_keyboard() -> InlineKeyboardMarkup:
    inline_markup = InlineKeyboardMarkup(1)

    for i, question in enumerate(questions.get_all()):
        b_inline = InlineKeyboardButton(question, callback_data=data_cb.new(id=i+1, action="get_answer"))
        inline_markup.add(b_inline)

    return inline_markup
