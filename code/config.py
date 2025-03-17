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

PERSONALITIES_DESCRIPTION = {
    "INTJ": {
        "description": "Стратег. Инновационный мыслитель с богатым воображением и стратегическим умом. "
                       "Всегда ищет способы улучшить системы и процессы.",
        "quote": "Я не боюсь штормов, ибо я учусь управлять своим кораблём. — Луиза Мэй Олкотт",
        "picture": "INTJ_architect.jpeg"
    },
    "INTP": {
        "description": "Логик. Любознательный и аналитичный, с неутолимой жаждой знаний. "
                       "Часто погружён в свои мысли и теории.",
        "quote": "Знание — это сила. — Фрэнсис Бэкон",
        "picture": "INTP_logician.jpeg"
    },
    "ENTJ": {
        "description": "Командир. Решительный и харизматичный лидер, "
                       "который любит испытания и умеет вдохновлять других.",
        "quote": "Лидерство — это искусство заставлять людей делать то, что вы хотите,"
                 " потому что они хотят этого. — Дуайт Эйзенхауэр",
        "picture": "ENTJ_commander.jpeg"
    },
    "ENTP": {
        "description": "Полемист. Остроумный и изобретательный, любит дебаты и новые идеи. "
                       "Всегда готов бросить вызов чьим то идеям.",
        "quote": "Посеешь мысль, пожнешь поступок; посеешь поступок, пожнешь привычку; посеешь привычку,"
                 " пожнешь характер; посеешь характер, пожнешь судьбу. — Стивен Кови",
        "picture": "ENTP_debater.jpeg"
    },
    "INFJ": {
        "description": "Активист. Идеалист с глубоким чувством цели и сострадания. Стремится сделать мир лучше.",
        "quote": "Будь тем изменением, которое ты хочешь видеть в мире. — Махатма Ганди",
        "picture": "INFJ_advocate.jpeg"
    },
    "INFP": {
        "description": "Мечтатель. Чувствительный и творческий, с сильным чувством морали и ценностей. "
                       "Мечтает о гармонии и понимании.",
        "quote": "Следуй за своим сердцем, но возьми с собой мозг. — Альфред Адлер",
        "picture": "INFP_mediator.jpeg"
    },
    "ENFJ": {
        "description": "Наставник. Харизматичный и вдохновляющий, с талантом мотивировать других. "
                       "Всегда стремится к гармонии и сотрудничеству.",
        "quote": "Лучший путь предсказать будущее — создать его. — Питер Друкер",
        "picture": "ENFJ_protagonist.jpeg"
    },
    "ENFP": {
        "description": "Компаньон. Энергичный и свободолюбивый, с энтузиазмом относится к новым идеям и возможностям."
                       " Любит вдохновлять других.",
        "quote": "Вдохновение - это умение приводить себя в рабочее состояние. - Александр Пушкин",
        "picture": "ENFP_campaigner.jpeg"
    },
    "ISTJ": {
        "description": "Инспектор. Ответственный и организованный, с сильным чувством долга. Ценит порядок и традиции.",
        "quote": "Мы в ответе за тех, кого не научили отвечать. - Кэтрин Прайс",
        "picture": "ISTJ_logistician.jpeg"
    },
    "ISFJ": {
        "description": "Защитник. Заботливый и преданный, всегда готов помочь другим. Ценит стабильность и гармонию.",
        "quote": "Маленькие добрые дела — это основа великих свершений. — Мать Тереза",
        "picture": "ISFJ_defender.jpeg"
    },
    "ESTJ": {
        "description": "Администратор. Практичный и решительный, с талантом организовывать и управлять. "
                       "Ценит эффективность и дисциплину.",
        "quote": "Действие — это ключ к успеху. — Пабло Пикассо",
        "picture": "ESTJ_executive.jpeg"
    },
    "ESFJ": {
        "description": "Консул. Дружелюбный и заботливый, с талантом создавать гармонию в коллективе. "
                       "Всегда стремится помочь другим.",
        "quote": "Счастье — это когда тебя понимают. — Станислав Троцкий",
        "picture": "ESFJ_consul.jpeg"
    },
    "ISTP": {
        "description": "Виртуоз. Практичный и гибкий, с талантом решать проблемы на лету. Любит свободу и эксперименты.",
        "quote": "Жить - значит делать вещи, а не приобретать их - Аристотель",
        "picture": "ISTP_virtuoso.jpeg"
    },
    "ISFP": {
        "description": "Композитор. Чувствительный и творческий, с любовью к красоте и гармонии. "
                       "Ценит свободу и самовыражение.",
        "quote": "Искусство — это выражение самых глубоких мыслей самым простым способом. — Альберт Эйнштейн",
        "picture": "ISFP_adventurer.jpeg"
    },
    "ESTP": {
        "description": "Предприниматель. Энергичный и амбициозный, с талантом находить возможности. "
                       "Любит действовать и преодолевать препятствия.",
        "quote": "В минуту нерешительности действуй быстро и старайся сделать первый шаг, "
                 "хоть бы и лишний — Лев Толстой",
        "picture": "ESTP_entreppreneur.jpeg"
    },
    "ESFP": {
        "description": "Развлекатель. Жизнерадостный и спонтанный, с талантом наслаждаться жизнью и вдохновлять других.",
        "quote": "Живи так, как будто это твой последний день, ведь один из них таким и окажется — Марк Аврелий",
        "picture": "ESFP_entertainer.jpeg"
    }
}