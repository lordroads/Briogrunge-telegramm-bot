from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove
from bot.init import bot
from keyboards import kb_client


async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет, что Вас интересует?', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Answer to message')


async def get_questions(message: types.Message):
    await bot.send_message(message.from_user.id, 'Тут будут вопросы', reply_markup=ReplyKeyboardRemove())
    await message.delete()


async def export_registration(message: types.Message):
    await bot.send_message(message.from_user.id, 'Тут будут регистрация вывоза вещей для клиента', reply_markup=ReplyKeyboardRemove())
    await message.delete()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(get_questions, commands=['Вопросы'])
    dp.register_message_handler(export_registration, commands=['Вывоз_вещей'])
