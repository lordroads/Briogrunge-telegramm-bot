from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


def get_inline_common_keyboard_subscribe() -> InlineKeyboardMarkup:
    inline_markup = InlineKeyboardMarkup(row_width=2)

    # TODO: Подготовить кнопки для запроса о рассылке новостей.
    # for i, question in enumerate(questions.get_all()):
    #     b_inline = InlineKeyboardButton(question, callback_data=data_cb.new(id=i+1, action="get_answer"))
    #     inline_markup.add(b_inline)

    return inline_markup
