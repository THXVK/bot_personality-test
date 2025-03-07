import asyncio

from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from data import users, questions
from keyboards import answers_kb

router = Router()
q_limit = 30


class Answer(StatesGroup):
    answer_call = State()
    question_call = State()
    paused = State()



#  todo: выбор сложности


@router.message(CommandStart())
async def start_message(message: Message):
    users[message.from_user.id] = {
        'q_num': 1,
        'axes': {
            'I - E': 0,
            'S - N': 0,
            'F - T': 0,
            'J - P': 0,
        },
        'p_type': 'untitled'
    }
    await message.reply('Привет!\nЭто бот-тест на тип личности, основанный на MBTI\n'
                        'Чтобы начать тест, напиши /start_test',
                        reply_markup=ReplyKeyboardRemove())  # todo: проверка на рестарт
    # todo: выбор сложности на {q_limit}
    print(message.user_id)
    print(message.chat.id)


@router.message(Command('help'))
async def send_commands_list(message: Message):
    await message.reply('список команд:')


@router.message(Command('start_test'))
async def send_first_question_text(message: Message, state: FSMContext):
    await state.set_state(Answer.answer_call)
    await message.reply(f'Вопрос 1/{q_limit}\n{questions[1]['text']}', reply_markup=answers_kb)


@router.message(Answer.answer_call)
async def send_confirmation_text(message: Message, state: FSMContext):
    await state.clear()
    user_id = message.user_id
    q_num = users[user_id]['q_num']
    axe = questions[q_num]['axe']

    if message.text in ['1', '2', '3', '4', '5']:
        answer = -1 + 0.5 * (int(message.text) - 1)
        users[user_id][axe][answer] += answer
        await message.reply('Принято!')
        users[user_id]['q_num'] += 1
        if q_num := users[user_id]['q_num'] > q_limit:
            pass  # todo: финал теста
        else:
            await send_next_question(message)

    elif message.text.startswith('/'):
        await message.reply('Для вызова команд напишите /stop')
        await send_next_question(message)
    elif message.text == '/stop_test':
        await message.reply('Вы остановили тест. Для его продолжения напишите /continue',
                            reply_markup=ReplyKeyboardRemove())
    else:
        await message.reply('Неверный ответ')
        await send_next_question(message)



async def send_next_question(message: Message, state: FSMContext):
    user_id = message.user_id
    q_number = users[user_id]['q_num']
    text = questions[q_number]['text']
    await message.reply(f'Вопрос {q_number}/{q_limit}\n{text}')
    await state.set_state()
    # todo: FSM states?


@router.message(Command('continue'))
async def continue_test(message: Message):
    user_id = message.user_id
    q_number = users[user_id]['q_num']
    await send_next_question(message)
