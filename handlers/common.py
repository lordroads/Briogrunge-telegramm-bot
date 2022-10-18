from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove
from bot.init import bot
from database import users
from models.user import User
from keyboards import client_kb


async def command_start(message: types.Message):
    await message.delete()
    # Проверить есть ли юзер
    find_user = users.get_user_by_id(message.from_user.id)

    if find_user:
        user = User(find_user)
        # Проверить админ ли юзер
        if user.is_admin:
            await bot.send_message(message.from_user.id,
                                   'Ты есть в базе и ты админ.',
                                   reply_markup=ReplyKeyboardRemove())
        else:
            await bot.send_message(message.from_user.id,
                                   f'Доброго времени суток, {user.first_name}, чем могу помочь?',
                                   reply_markup=client_kb.get_markup_client_menu())
    else:
        await bot.send_message(message.from_user.id,
                               'Привет, что Вас интересует?',
                               reply_markup=client_kb.get_markup_client_menu())
        users.add_user(message.from_user.id,
                       message.from_user.is_bot,
                       False,
                       message.from_user.first_name,
                       message.from_user.last_name,
                       message.from_user.username,
                       message.from_user.language_code)


async def clear_history(message: types.Message):
    await message.delete()


async def leave_chat(chat_member: types.ChatMemberUpdated):
    find_user = users.get_user_by_id(chat_member.from_user.id)
    if find_user:
        user = User(find_user)
        if not bool(user.is_admin) and chat_member.new_chat_member.status == 'kicked':
            users.delete_user(user.user_id)

            print(f'[EVENT old] - USER=user.id {chat_member.old_chat_member}\n\n')
            print(f'[EVENT new] - USER=user.id {chat_member.new_chat_member}\n\n')
            print(f'[USER id] - USER=user.id {chat_member.from_user.id}\n\n')


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'menu'])
    dp.register_message_handler(clear_history)
    dp.register_my_chat_member_handler(leave_chat)
