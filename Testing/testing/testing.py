import threading
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext

# Sessiestatus
SESSION_ACTIVE = 1
SESSION_INACTIVE = 0

# Functie om de sessie te starten
def start_session(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    context.user_data[user_id] = SESSION_ACTIVE
    update.message.reply_text("Sessie gestart. Je kunt nu typen. Je hebt 10 seconden.")

    # Stel een timer in om de sessie na 10 seconden te beëindigen
    def end_session():
        user_id = update.message.from_user.id
        if context.user_data.get(user_id) == SESSION_ACTIVE:
            context.user_data[user_id] = SESSION_INACTIVE
            update.message.reply_text("Sessie beëindigd. Je kunt niet meer typen.")

    timer = threading.Timer(10, end_session)
    timer.start()

# Functie om berichten te verwerken tijdens een actieve sessie
def handle_message(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    if context.user_data.get(user_id) == SESSION_ACTIVE:
        text = update.message.text
        update.message.reply_text(f"Je zei: {text}")

def main():
    # Vervang 'YOUR_BOT_TOKEN' door de echte bot-token
    updater = Updater(token='6501001622:AAFANqsidVQxue1Tlh6rPhDK6sT4DHxNUBs', use_context=True)
    dispatcher = updater.dispatcher

    # Voeg de commando-handler toe
    start_handler = CommandHandler('start', start_session)
    dispatcher.add_handler(start_handler)

    # Voeg de berichtenhandler toe
    message_handler = MessageHandler(Filters.text & ~Filters.command, handle_message)
    dispatcher.add_handler(message_handler)

    # Start de bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()