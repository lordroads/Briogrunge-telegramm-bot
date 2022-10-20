from aiogram import types, Dispatcher
from bot.init import bot
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from database import questions


class FSMAddQuestion(StatesGroup):
    question = State()
    answer = State()


async def cancel(message: types.Message, state: FSMContext):
    await message.delete()
    current_state = await state.get_state()

    if current_state is None:
        return

    await state.finish()
    await bot.send_message(message.from_user.id, 'Okey')


async def add_question(message: types.Message):
    await FSMAddQuestion.question.set()
    await bot.send_message(message.from_user.id, 'Начнём. Напишите часто задаваемый вопрос.')


async def add_answer(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question'] = message.text
    await FSMAddQuestion.next()
    await bot.send_message(message.from_user.id, 'Окей, теперь напишите ответ для этого вопроса.')


async def finish_question(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['answer'] = message.text
        questions.add_question(data["question"], data["answer"])
        await bot.send_message(message.from_user.id, f'Добавили в базу:\n\nВопрос:\n{data["question"]}\nОтвет:\n{data["answer"]}')

    await state.finish()


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cancel, state='*', commands='Отмена')
    dp.register_message_handler(cancel, Text(equals='Отмена', ignore_case=True), state='*')
    dp.register_message_handler(add_question, Text(equals='Добавить вопрос'), state=None)
    dp.register_message_handler(add_answer, state=FSMAddQuestion.question)
    dp.register_message_handler(finish_question, state=FSMAddQuestion.answer)

