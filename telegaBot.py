import getAnswerByIntent
import getStub
import classifyIntent
import botConfig

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi!')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Help!')

def run_bot(update: Update, context: CallbackContext) -> None:
    response = bot(update.message.text)
    update.message.reply_text(response)

def bot(replica):
    # NLU
    intent = classifyIntent.classify_intent(replica)
    # Получение ответа
    # Правила:
    if intent:
        answer = getAnswerByIntent.get_answer_by_intent(intent)
        if answer:
            return answer
    # Заглушка
    answer = getStub.get_stub()
    return answer

def main():
    updater = Updater("1648878552:AAHv6DiWSHdUtYuQ6kQrUADuaxYML3vVKZQ")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, run_bot))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
