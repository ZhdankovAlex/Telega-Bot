import botConfig
import random

def get_answer_by_intent(intent):
    if intent in botConfig.BOT_CONFIG['intents']:
        responses = botConfig.BOT_CONFIG['intents'][intent]['responses']
        return random.choice(responses)
