import asyncio

from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from data import q_data, users, questions
from keyboards import answers_kb

router = Router()


#  todo: выбор сложности

@router.message(CommandStart())
async def start_message(message: Message):
    await message.reply('Привет!\nЭто бот-тест на тип личности, основанный на MBTI\n'
                        'Чтобы начать тест, напиши /start_test')
    print(message.user_id)
    print(message.chat.id)


@router.message(Command('help'))
async def send_commands_list(message: Message):
    await message.reply('список команд:')


@router.message(Command('start_test'))
async def send_first_question_text(message: Message):
    await message.reply(f'вопрос 1\n{q_data[1]}', reply_markup=answers_kb)

@router.message(Command('continue'))
async def continue_test(message: Message):
    user_id = message.user_id
    q_number = users[user_id]['q_num']
    await send_next_question(message, q_number)


@router.message()
async def send_confirmation_text(message: Message):
    user_id = message.user_id
    q_num = users[user_id]['q_num']
    axe = questions[q_num]['axe']

    if message.text in ['1', '2', '3', '4', '5']:
        answer = -1 + 0.5 * (int(message.text) - 1)
        users[user_id][axe][answer] += answer
        ...
    elif message.text == '/stop_test':
        await message.reply('вы остановили тест. Для его продолжения напишите /continue',
                            reply_markup=ReplyKeyboardRemove())
    else:
        await message.reply('неверный ответ')
        ...


async def send_next_question(message, q_number):
