import asyncio

from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from data import users, questions, base_letters
from keyboards import answers_kb

router = Router()
q_limit = 5


class TestStages(StatesGroup):
    answer_call = State()
    answer_processing = State()
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
    await message.answer('Привет!\nЭто бот-тест на тип личности, основанный на MBTI\n'
                        'Чтобы начать тест, напиши /start_test',
                        reply_markup=ReplyKeyboardRemove())  # todo: проверка на рестарт
    # todo: выбор сложности на {q_limit}



@router.message(Command('help'))
async def send_commands_list(message: Message):
    await message.answer('список команд:')


@router.message(Command('start_test'))
async def send_first_question_text(message: Message, state: FSMContext):
    await message.answer(f'Вопрос 1/{q_limit}\n{questions[1]['text']}', reply_markup=answers_kb)
    await state.set_state(TestStages.answer_call)


@router.message(TestStages.answer_call)
async def send_confirmation_text(message: Message, state: FSMContext):
    await state.set_state(TestStages.answer_processing)
    user_id = message.from_user.id
    q_num = users[user_id]['q_num']
    axe = questions[q_num]['axe']

    if message.text in ['1', '2', '3', '4', '5']:
        answer = -1 + 0.5 * (int(message.text) - 1)
        users[user_id]['axes'][axe] += answer
        await message.answer('Принято!')
        users[user_id]['q_num'] += 1
        q_num = users[user_id]['q_num']

        if q_num > q_limit:
            persona = ''
            for letters, value in users[user_id]['axes'].items():
                l_1, l_2 = letters.split(' - ')

                if value < 0:
                    persona += l_1

                elif value > 0:
                    persona += l_2

                else:
                    letter = base_letters[letters]
                    persona += letter
            await message.answer(f'ваш тип: {persona}',
                                 reply_markup=ReplyKeyboardRemove())
            await state.clear()
        else:
            await state.set_state(TestStages.question_call)
            await send_next_question(message, state)

    elif message.text == '/stop_test':
        await message.answer('Вы остановили тест. Для его продолжения напишите /continue',
                             reply_markup=ReplyKeyboardRemove())
    elif message.text.startswith('/'):
        await message.answer('Для вызова команд напишите /stop')
        await send_next_question(message, state)

    else:
        await message.answer('Неверный ответ')
        await send_next_question(message, state)


@router.message(TestStages.question_call)
async def send_warning_message_1(message: Message):
    await message.answer('подождите отправки вопроса')


@router.message(TestStages.answer_processing)
async def send_warning_message_2(message: Message):
    await message.answer('подождите обработки ответа')


@router.message(TestStages.question_call)
async def send_next_question(message: Message, state: FSMContext):
    user_id = message.from_user.id
    q_number = users[user_id]['q_num']
    text = questions[q_number]['text']
    await message.answer(f'Вопрос {q_number}/{q_limit}\n{text}')
    await state.set_state(TestStages.answer_call)


@router.message(Command('continue'))
async def continue_test(message: Message, state: FSMContext):
    user_id = message.from_user.id
    q_number = users[user_id]['q_num']
    await send_next_question(message, state)
