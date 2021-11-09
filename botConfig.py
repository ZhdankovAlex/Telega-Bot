BOT_CONFIG = {
    'failure_phrases': [
        'сформулируй точнее',
        'неправильный ответ, либо попробуй написать фразу полностью',
        'неверный или недостаточно полный ответ'
    ],
    'intents': {
        'hello': {
            'examples': [
                'Привет',
            ],
            'responses': [
                'Привет, Нэнси Дрю)',
            ],
        },
        'bye': {
            'examples': [
                'Пока',
            ],
            'responses': [
                'I <3 you \n'
                "18 31'45.15,70 15'0.0",
            ],
        },
        # 18 - http://qrcoder.ru/code/?18&10&0
        'syaki-myaki': {
            'examples': [
                'Рок-н-роллы',
                'Рокнроллы',
                'Рок н роллы',
            ],
            'responses': [
                'Приезжай в Казань',
            ],
        },
        #  - для пробела нет QR кода
        'nut-beer': {
            'examples': [
                'Друзья',
                'Бар Друзья',
            ],
            'responses': [
                'Enjoy The Now',
            ],
        },
        # 31' - http://qrcoder.ru/code/?31%27&10&0
        'mosque': {
            'examples': [
                'Мечеть',
                'Мечеть Кул-Шариф',
                'Мечеть Кул Шариф',
            ],
            'responses': [
                'Мечеть Кул Шариф',
            ],
        },
        # 45. - http://qrcoder.ru/code/?45.&10&0
        'port': {
            'examples': [
                'Порт',
                'Порт Севкабель',
                'Севкабель-Порт',
                'Севкабель Порт',
            ],
            'responses': [
                'Море волнуется и скучает',
            ],
        },
        # 15"S - http://qrcoder.ru/code/?15%22S&10&0
        'zinger': {
            'examples': [
                'Зингер',
                'Подписные издания',
            ],
            'responses': [
                'Подписные издания',
            ],
        },
        # , - http://qrcoder.ru/code/?%2C&10&0
        'water-tower': {
            'examples': [
                'Башня',
                'Водонапорная башня',
            ],
            'responses': [
                'Главное, чтобы дома кто-то ждал',
            ],
        },
        # 70 - http://qrcoder.ru/code/?70&10&0
        'curonian-spit': {
            'examples': [
                'Куршская коса',
                'Коса',
            ],
            'responses': [
                'Нерпы',
            ],
        },
        # - для пробела нет QR кода
        'bfu': {
            'examples': [
                'Балтийский федеральный университет имени Иммануила Канта',
                'БФУ',
            ],
            'responses': [
                'Сейчас бы к морю, а не вот это вот всё',
            ],
        },
        # 15' - http://qrcoder.ru/code/?15%27&10&0
        'bakery': {
            'examples': [
                'Хлебзавод',
            ],
            'responses': [
                'Наша фотография',
            ],
        },
        # 0. - http://qrcoder.ru/code/?0.&10&0
        'vdnh': {
            'examples': [
                'ВДНХ',
            ],
            'responses': [
                'Кот с TEXTIL',
            ],
        },
        # 0"W - http://qrcoder.ru/code/?0%22W&10&0
        'lake': {
            'examples': [
                'Плещеево',
                'Плещеево озеро',
            ],
            'responses': [
                'Чайку?',
            ],
        },
        # 18 31'45.15"S , 70 15'0.0"W
    },
}
