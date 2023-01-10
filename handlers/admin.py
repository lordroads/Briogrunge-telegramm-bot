from aiogram import types, Dispatcher
from aiogram.types import CallbackQuery
from bot.init import bot
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from database import questions
from keyboards import admin_kb


class FSMAddQuestion(StatesGroup):
    question = State()
    answer = State()


class FSMUpdateQuestion(StatesGroup):
    question_id = State()
    question = State()
    answer = State()


async def cancel(message: types.Message, state: FSMContext):
    await message.delete()
    current_state = await state.get_state()

    if current_state is None:
        return

    await state.finish()
    await bot.send_message(message.from_user.id, 'Okey')


async def get_list_delete_questions(message: types.Message):
    await message.delete()
    await bot.send_message(message.from_user.id,
                           'Выберите вопрос для удаления:',
                           reply_markup=admin_kb.get_inline_questions_keyboard("delete_question"))


async def delete_question(callback_query: CallbackQuery, callback_data: dict):
    await callback_query.message.delete()
    question_id = int(callback_data.get("id"))
    entity = questions.get_question_by_id(question_id)
    await bot.answer_callback_query(callback_query.id)
    questions.delete_question(question_id)
    await bot.send_message(callback_query.from_user.id,
                           f'{question_id}.\n{entity[1]}\n{entity[2]}\n\nВопрос №{question_id} удален!')


async def get_list_update_questions(message: types.Message):
    await FSMUpdateQuestion.question_id.set()
    await bot.send_message(message.from_user.id,
                           'Выберите вопрос для обновления:',
                           reply_markup=admin_kb.get_inline_questions_keyboard("update_question"))


async def update_question(callback_query: CallbackQuery, callback_data: dict, state: FSMContext):
    await callback_query.message.delete()
    question_id = int(callback_data.get("id"))
    entity = questions.get_question_by_id(question_id)
    await bot.answer_callback_query(callback_query.id)

    async with state.proxy() as data:
        data['question_id'] = question_id

    await FSMUpdateQuestion.next()
    await bot.send_message(callback_query.from_user.id, f'Что изменить в этом вопросе:\n\n"{entity[1]}"')


async def update_answer(message: types.Message, state: FSMContext):
    if message.text:
        async with state.proxy() as data:
            data['question'] = message.text
        await FSMUpdateQuestion.next()
        await bot.send_message(message.from_user.id, 'Напишите обновленный ответ для этого вопроса.')
    else:
        await bot.send_message(message.from_user.id, 'Повторите ввод вопроса, так как что то пошло не так.')


async def finish_update_question(message: types.Message, state: FSMContext):
    if message.text:
        async with state.proxy() as data:
            data['answer'] = message.text
            questions.update_question(data['question'], data['answer'], data['question_id'])
            await bot.send_message(message.from_user.id, f'Обновлен вопрос ID-№{data["question_id"]}')
        await state.finish()
    else:
        await bot.send_message(message.from_user.id, 'Повторите ввод ответа, так как что то пошло не так.')


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

    dp.register_message_handler(get_list_delete_questions, Text(equals='Удалить вопрос'))
    dp.register_callback_query_handler(delete_question, admin_kb.data_cb.filter(action=["delete_question"]))

    dp.register_message_handler(get_list_update_questions, Text(equals='Редактировать вопрос'), state=None)
    dp.register_callback_query_handler(update_question,admin_kb.data_cb.filter(action=["update_question"]), state=FSMUpdateQuestion.question_id)
    dp.register_message_handler(update_answer, state=FSMUpdateQuestion.question)
    dp.register_message_handler(finish_update_question, state=FSMUpdateQuestion.answer)

    dp.register_message_handler(add_question, Text(equals='Добавить вопрос'), state=None)
    dp.register_message_handler(add_answer, state=FSMAddQuestion.question)
    dp.register_message_handler(finish_question, state=FSMAddQuestion.answer)

