import random
import nltk

BOT_CONFIG = {
    'failure_phrases': [
        'Чаво-чаво? Не слыхать, говори громче!',
        'Ты чево несёшь-то, пёс ополоумевший?'
        'Я о таком не слыхала',
        'Поди-ка отсюдова с такими вопросами',
        'Вроде по-русски говоришь, а ничево не поняла',
        'Ты нормально растолкуй, я не поняла',
        'Белены, чай, объелся, коли такую несусветицу несёшь...',
        'Ты если спросить чаво хочешь, то давай конкретнее',
        'Нашёл кого спросить...',
        '   .0_о.     (?)',
    ],
    'intents': {
        'hello': {
            'examples': [
                'Привет',
                'Здравствуйте',
                'Здравствуй',
                'Здравствуй Баба Маня',
                'Привет Баба Маня',
                'Здравствуйте Баба Маня',
                'Здравствуй Баб Мань',
                'Привет Баб Мань',
                'Здравствуйте Баб Мань',
                'Доброе утро'
                'Добрый день',
                'Добрый вечер',
                'Доброе утро Баба Маня'
                'Добрый день Баба Маня',
                'Добрый вечер Баба Маня',
                'Доброе утро Баб Мань'
                'Добрый день Баб Мань',
                'Добрый вечер Баб Мань',
                'Ку',
                'Ку-ку',
                'Здарова',
                'Здарова, кума',
                'Шалом',
                'Приветики',
                'Хэллоу',
                'Хай',
            ],
            'responses': [
                'Привет',
                'Здравствуйте',
                'Здравствуй',
                'Привет, внучек',
                'Заждалась баушка, не приходили давно',
                'Ты ежели по делу зашёл, то спрашивай',
                'Доброе утро'
                'Добрый день',
                'Добрый вечер',
            ],
        },
        'bye': {
            'examples': [
                'Пока',
                'До свидания',
                'Прощай',
                'Пока Баба Маня',
                'До свидания Баба Маня',
                'Прощай Баба Маня',
                'Пока Баб Мань',
                'До свидания Баб Мань',
                'Прощай Баб Мань',
                'Покедова',
                'До встречи, кума',
                'Бай',
                'Гудбай',
            ],
            'responses': [
                'Пока',
                'Прощай',
                'До свидания',
                'Пока, внучек',
                'Буду ждать новой встречи',
                'Ещё свидимся',
            ],
        },
    },
}

def bot(replica):
    # NLU
    intent = classify_intent(replica)

    # Получение ответа
    # Правила:
    if intent:
        answer = get_answer_by_intent(intent)
        if answer:
            return answer
    # Генеративная модель:
    answer = generate_answer(replica)
    if answer:
        return answer
    # Заглушка
    answer = get_stub()
    return answer

def classify_intent(replica):
    # Приводим текст к низкому регистру, убираем знаки препинания
    replica = clear_text(replica)
    for intent, intent_data in BOT_CONFIG['intents'].items():
        for example in intent_data['examples']:
            example = clear_text(example)
            # Вычисляем редакционное расстояние
            distance = nltk.edit_distance(replica, example)
            if distance / len(example) < 0.3:
                return intent

def get_answer_by_intent(intent):
    if intent in BOT_CONFIG['intents']:
        responses = BOT_CONFIG['intents'][intent]['responses']
        return random.choice(responses)

def generate_answer(replica):
    # TODO
    return 'hello, how are you?'

def get_stub():
    failure_phrases = BOT_CONFIG['failure_phrases']
    return random.choice(failure_phrases)

def clear_text(text):
    text = text.lower()
    еуче = ''.join([char for char in text if char in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя -'])
    return text

print(bot('Здарова, кума'))
