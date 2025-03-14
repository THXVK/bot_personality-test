from dotenv import load_dotenv
from os import getenv
# todo: создать .env шаблон файла для github
# todo: docker файл

load_dotenv()
TOKEN = getenv('TOKEN')

MID_LIMIT = 32



QUESTIONS = {
    1: {
        'text': 'составляю списки | полагаюсь на память',
        'axe': 'J - P'
    },
    2: {
        'text': 'настроен скептически | хочу верить',
        'axe': 'F - T'
    },
    3: {
        'text': 'нуждаюсь в одиночестве | скучаю в нем',
        'axe': 'I - E'
    },
    4: {
        'text': 'принимаю все как есть | недоволен положением вещей',
        'axe': 'F - T'
    },
    5: {
        'text': 'порядок в комнате | разбрасываю вещи',
        'axe': 'J - P'
    },
    6: {
        'text': 'сравнение с роботом для меня обидно | стремлюсь мыслить как механизм',
        'axe': 'F - T'
    },
    7: {
        'text': 'мягкий | энергичный',
        'axe': 'I - E'
    },
    8: {
        'text': 'написать эссе | пройти тест',
        'axe': 'J - P'
    },
    9: {
        'text': 'хаотичный | организованный',
        'axe': 'J - P'
    },
    10: {
        'text': 'легкоранимый | толстокожий',
        'axe': 'F - T'
    },
    11: {
        'text': 'работа самостоятельно | работа в коллективе',
        'axe': 'I - E'
    },
    12: {
        'text': 'фокус на будущем | фокус на настоящем',
        'axe': 'S - N'
    },
    13: {
        'text': 'планирую наперед | решаю в последнюю минуту',
        'axe': 'J - P'
    },
    14: {
        'text': 'меня уважают | меня любят',
        'axe': 'F - T'
    },
    15: {
        'text': 'вечеринки утомляют | заряжаюсь бодростью на них',
        'axe': 'I - E'
    },
    16: {
        'text': 'вписываюсь в коллектив | держусь особняком',
        'axe': 'I - E'
    },
    17: {
        'text': 'оставляю себе свободу выбора | беру обязательства на себя',
        'axe': 'J - P'
    },
    18: {
        'text': 'хочу чинить вещи | хочу исправлять людей',
        'axe': 'F - T'
    },
    19: {
        'text': 'говорю | слушаю',
        'axe': 'I - E'
    },
    20: {
        'text': 'опишу событие | перескажу его смысл',
        'axe': 'S - N'
    },
    21: {
        'text': 'работаю сразу | откладываю на потом',
        'axe': 'J - P'
    },
    22: {
        'text': 'слушаю сердце | слушаю рассудок',
        'axe': 'F - T'
    },
    23: {
        'text': 'сижу дома | провожу время вне дома',
        'axe': 'I - E'
    },
    24: {
        'text': 'видеть общую картину | видеть детали',
        'axe': 'S - N'
    },
    25: {
        'text': 'импровизирую | готовлюсь',
        'axe': 'J - P'
    },
    26: {
        'text': 'справедливость | сострадание',
        'axe': 'F - T'
    },
    27: {
        'text': 'не люблю кричать | могу крикнуть кому-то на расстоянии',
        'axe': 'I - E'
    },
    28: {
        'text': 'теоретик | практик',
        'axe': 'S - N'
    },
    29: {
        'text': 'делаю дело | гуляю смело',
        'axe': 'I - E'
    },
    30: {
        'text': 'дискомфорт от эмоций | ценю их',
        'axe': 'F - T'
    },
    31: {
        'text': 'люблю выступать | избегаю публики',
        'axe': 'I - E'
    },
    32: {
        'text': 'Что? Где? Когда? | Почему?',
        'axe': 'S - N'
    },
}

BASE_LETTERS = {
            'I - E': 'I',
            'S - N': 'N',
            'F - T': 'T',
            'J - P': 'J',
}
