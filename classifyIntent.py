import nltk
import botConfig

def clear_text(text):
    text = text.lower()
    text = ''.join([char for char in text if char in '1234567890абвгдеёжзийклмнопрстуфхцчшщъыьэюя -'])
    return text

def classify_intent(replica):
    # Приводим текст к низкому регистру, убираем знаки препинания
    replica = clear_text(replica)
    for intent, intent_data in botConfig.BOT_CONFIG['intents'].items():
        for example in intent_data['examples']:
            example = clear_text(example)
            # Вычисляем редакционное расстояние
            distance = nltk.edit_distance(replica, example)
            if distance / len(example) < 0.1:
                return intent
