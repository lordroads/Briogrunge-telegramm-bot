from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher.filters import Text
from bot.init import bot
from keyboards import client_kb
from database import questions


async def get_questions(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Часто задаваемые вопросы:',
                           reply_markup=client_kb.get_inline_questions_keyboard())
    await message.delete()


async def get_answer(callback_query: CallbackQuery, callback_data: dict):
    await callback_query.message.delete()
    question_id = int(callback_data.get("id"))
    await bot.answer_callback_query(callback_query.id)
    question = questions.get_question_by_id(question_id)
    await bot.send_message(callback_query.from_user.id, f'{question[1]}\n\n{question[2]}')


async def export_registration(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Тут будут регистрация вывоза вещей для клиента, в данные момент этот раздел не работает.')
    await message.delete()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(get_questions, Text(equals='Вопросы'))
    dp.register_message_handler(export_registration, Text(equals='Вывоз_вещей'))
    dp.register_callback_query_handler(get_answer, client_kb.data_cb.filter(action=["get_answer"]))
