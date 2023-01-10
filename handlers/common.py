from aiogram import types, Dispatcher
from aiogram.types import CallbackQuery
from bot.init import bot
from database import users
from models.user import User
from keyboards import client_kb, admin_kb, common_kb


async def command_start(message: types.Message):
    await message.delete()
    find_user = users.get_user_by_id(message.from_user.id)

    if find_user:
        user = User(find_user)
        if user.is_admin:
            await bot.send_message(message.from_user.id,
                                   'Ты есть в базе и ты админ.',
                                   reply_markup=admin_kb.get_markup_admin_menu())
        else:
            await bot.send_message(message.from_user.id,
                                   f'Доброго времени суток, {user.first_name}, чем могу помочь?',
                                   reply_markup=client_kb.get_markup_client_menu())
    else:
        await bot.send_message(message.from_user.id,
                               'Привет, что Вас интересует?',
                               reply_markup=client_kb.get_markup_client_menu())
        # TODO: сделать инлайн с вопросом об рассылке ивентов.
        users.add_user(message.from_user.id,
                       message.from_user.is_bot,
                       False,
                       message.from_user.first_name,
                       message.from_user.last_name,
                       message.from_user.username,
                       message.from_user.language_code)


async def clear_history(message: types.Message):
    await message.delete()


async def all_callbacks(callback_query: CallbackQuery):
    await callback_query.message.delete()
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f'Усп! попробуйте еще раз...')


async def leave_chat(chat_member: types.ChatMemberUpdated):
    find_user = users.get_user_by_id(chat_member.from_user.id)
    if find_user:
        user = User(find_user)
        if not bool(user.is_admin) and chat_member.new_chat_member.status == 'kicked':
            users.delete_user(user.user_id)


def register_handlers_common(dp: Dispatcher):
    dp.register_callback_query_handler(all_callbacks)
    dp.register_message_handler(command_start, commands=['start', 'menu'])
    dp.register_message_handler(clear_history)
    dp.register_my_chat_member_handler(leave_chat)
