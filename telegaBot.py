import getAnswerByIntent
import getStub
import generateAnswer
import classifyIntent
import botConfig

def bot(replica):
    # NLU
    intent = classifyIntent.classify_intent(replica)

    # Получение ответа
    # Правила:
    if intent:
        answer = getAnswerByIntent.get_answer_by_intent(intent)
        if answer:
            return answer
    # Генеративная модель:
    answer = generateAnswer.generate_answer(replica)
    if answer:
        return answer
    # Заглушка
    answer = getStub.get_stub()
    return answer

print(bot('Здарова, кума'))
