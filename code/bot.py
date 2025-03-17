import asyncio
from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from keyboards import answers_kb
from config import QUESTIONS, BASE_LETTERS, PERSONALITIES_DESCRIPTION
from data import add_user, get_data, update_user_data, async_s


router = Router()
q_limit = 5


class TestStages(StatesGroup):
    answer_call = State()
    answer_processing = State()
    question_call = State()
    paused = State()


@router.message(CommandStart())
async def start_message(message: Message):
    user_id = message.from_user.id
    if await add_user(async_s, user_id):
        await message.answer('Привет!\nЭто бот-тест на тип личности, основанный на MBTI\n'
                             'Чтобы начать тест, напиши /start_test',
                             reply_markup=ReplyKeyboardRemove())  # todo: проверка на рестарт
    else:
        await message.answer('Вы уже зарегистрированы. '
                             'Если вы хотите пройти тест заново, то используйте команду /restart')


@router.message(Command('restart'))
async def restart(message: Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    await update_user_data(async_s, user_id, 'p_type', 'untitled')
    await update_user_data(async_s, user_id, 'q_num', 1)
    await send_first_question_text(message, state)


@router.message(Command('help'))
async def send_commands_list(message: Message):
    await message.answer('список команд:\n'
                         '/start - стартовая команда для регистрации\n'
                         '/restart - команда для прохождения теста заново\n'
                         '/start_test - команда для начала прохождения теста\n'
                         '/stop_test - служит для остановки прохождения теста\n'
                         '/continue - нужна для продолжения начатого теста\n'
                         '/help - отправляет список команд с их описанием')


@router.message(Command('start_test'))
async def send_first_question_text(message: Message, state: FSMContext):
    user_id = message.from_user.id
    data = await get_data(async_s, user_id)
    if data['p_type'] != 'untitled' and data['q_num'] != 1:
        await message.answer('для прохождения теста заново используйте /restart, а для продолжения - /continue')
        await message.answer(f'Вопрос 1/{q_limit}\n{QUESTIONS[1]['text']}', reply_markup=answers_kb)
        await state.set_state(TestStages.answer_call)


@router.message(TestStages.answer_call)
async def send_confirmation_text(message: Message, state: FSMContext):
    await state.set_state(TestStages.answer_processing)
    user_id = message.from_user.id
    user = await get_data(async_s, user_id)
    q_num = user['q_num']
    axe = QUESTIONS[q_num]['axe']

    if message.text in ['1', '2', '3', '4', '5']:
        answer = -1 + 0.5 * (int(message.text) - 1)
        user[axe] += answer
        await message.answer('Принято!')
        await update_user_data(async_s, user_id, 'q_num', q_num + 1)
        user = await get_data(async_s, user_id)
        q_num = user['q_num']

        if q_num > q_limit:
            msg = await message.answer('подождите.')
            persona = ''
            for letters, value in user['axes'].items():
                await msg.edit_text('подождите.' + '.' * len(persona))
                l_1, l_2 = letters.split(' - ')

                if value < 0:
                    persona += l_1

                elif value > 0:
                    persona += l_2

                else:
                    letter = BASE_LETTERS[letters]
                    persona += letter
                    
                await update_user_data(async_s, user_id, 'p_type', persona)
            with open(f'../{PERSONALITIES_DESCRIPTION[persona]['picture']}') as photo:
                await message.send_photo(photo=photo, caption=f'''ваш тип: {persona}.

{PERSONALITIES_DESCRIPTION[persona]['quote']}

{PERSONALITIES_DESCRIPTION[persona]['description']}''',
                                         reply_markup=ReplyKeyboardRemove())
                await message.answer('Если вы хотите пройти более подробный тест, или узнать больше о своем типе'
                                     ' личности, то посетите сайт 16personalities.com')
                await state.clear()
        else:
            await state.set_state(TestStages.question_call)
            await send_next_question(message, state)

    elif message.text == '/stop_test':
        await message.answer('Вы остановили тест. Для его продолжения напишите /continue',
                             reply_markup=ReplyKeyboardRemove())
    elif message.text.startswith('/'):
        await message.answer('Для вызова команд напишите /stop_test')
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
    user = await get_data(async_s, user_id)
    q_number = user['q_num']
    text = QUESTIONS[q_number]['text']
    await message.answer(f'Вопрос {q_number}/{q_limit}\n{text}')
    await state.set_state(TestStages.answer_call)


@router.message(Command('continue'))
async def continue_test(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = await get_data(async_s, user_id)
    q_number = user['q_num']
    if q_number == 1 or q_number == 32:
        await message.answer('У вас нет активных тестов')
    await send_next_question(message, state)
