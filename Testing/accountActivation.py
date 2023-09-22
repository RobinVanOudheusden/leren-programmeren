from telegram import Update
from telegram.ext import ConversationHandler, CallbackContext
import pymongo
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import string

# Connect to MongoDB database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["triplence-telegram-bot"]
mycol = mydb["registrations"]

def start(update: Update, context: CallbackContext):
    # Generate 5 character long random registration code.
    registration_code_characters = string.digits
    registration_code_characters = ''.join(random.choice(registration_code_characters) for i in range(5))
    print(registration_code_characters)

    # Use the Telegram Bot API to get user information
    user = update.message.from_user

    # Check if the user is already registered
    if mycol.find_one({"user_id": user.id}, {"user_id": 1}):
        update.message.reply_text("U bent al geregistreerd. Gebruik /help om verder te gaan!")
    else:
        update.message.reply_text("Welkom bij de registratie in onze bot!\nVoer de registratie code in die u heeft ontvangen:")
        registration_code = update.message.text

        if registration_code == registration_code_characters:
            update.message.reply_text("Registratie code is correct!")
        

