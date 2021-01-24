import botConfig
import random

def get_stub():
    failure_phrases = botConfig.BOT_CONFIG['failure_phrases']
    return random.choice(failure_phrases)
