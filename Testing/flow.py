from accountActivation import * 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def main():
    print("[BROADCAST] *** TELEGRAM BOT IS RUNNING... ***")
    # Bot Token
    updater = Updater(token='6367764011:AAEwwmG6lrWzorqGL7Af8UPkBOUDvomRdmM', use_context=True)
    dispatcher = updater.dispatcher

    # Define a command handler to start the conversation
    dispatcher.add_handler(CommandHandler('start', start))

    # Define a message handler to handle the user's response
    dispatcher.add_handler(MessageHandler(Filters.text, start))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()