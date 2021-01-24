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
    # TODO
    return 'hello'

def get_answer_by_intent(intent):
    # TODO
    return 'hello, human'

def generate_answer(replica):
    # TODO
    return 'hello, how are you?'

def get_stub():
    failure_phrases = [
        'Could not understand you',
        'Rewrite please',
        'Eror 404'
    ]
    # TODO
    return failure_phrases[0]
