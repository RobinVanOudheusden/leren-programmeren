from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext
import pymongo
import random
import string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define states for the conversation
REGISTRATION_CODE = range(1)

# Connect to MongoDB database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["triplence-telegram-bot"]
mycol1 = mydb["new_email_registrations"]
mycol = mydb["registrations"]

# Generate 5 character long random registration code
registration_code_characters = string.digits
registration_code_characters = ''.join(random.choice(registration_code_characters) for i in range(5))

# Define your email configuration
EMAIL_ADDRESS = 'robin.supraenet@gmail.com'  # Your email address
EMAIL_PASSWORD = 'dijc uzfw goww qvhw'         # Your email password
SMTP_SERVER = 'smtp.gmail.com'           # SMTP server (for Gmail)
SMTP_PORT = 587                          # SMTP port (for Gmail)

# Function to send an email with the registration code
def send_email(to_email, registration_code):
    subject = 'Registration Code for Telegram Bot'
    message = f'Your registration code is: {registration_code}'
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"Email could not be sent: {str(e)}")
        return False


def setup_registration(update: Update, context: CallbackContext):
    to_email = mycol1.find_one({}, {"_id": 0, "email": 1})
    if to_email:
        to_email = to_email["email"]
        print(to_email)
        send_email(to_email, registration_code_characters)
        update.message.reply_text("Een registratiecode is verzonden naar uw e-mailadres. Voer de code in om te voltooien:")
        return REGISTRATION_CODE
    else:
        print("No email found in the database")

# Define a function to handle user's registration code input
def receive_registration_code(update: Update, context: CallbackContext):
    to_email = mycol1.find_one({}, {"_id": 0, "email": 1})
    to_email = to_email["email"]
    user_id = update.message.from_user.id
    registration_code = update.message.text

    # Check if the provided code matches the generated code
    if registration_code == registration_code_characters:
        # Save the user's registration data in the database
        mycol.insert_one({"user_id": user_id, "email": to_email})
        update.message.reply_text("U bent succesvol geregistreerd!")
        mycol1.delete_one({"email": to_email})
    elif registration_code != registration_code_characters:
        update.message.reply_text("De registratiecode is onjuist. Probeer het opnieuw.")
        return REGISTRATION_CODE

def main():
    # Initialize the bot
    updater = Updater(token='6367764011:AAEwwmG6lrWzorqGL7Af8UPkBOUDvomRdmM', use_context=True)
    dispatcher = updater.dispatcher

    # Create a ConversationHandler to manage the registration process
    registration_handler = ConversationHandler(
        entry_points=[CommandHandler('start', setup_registration)],
        states={
            REGISTRATION_CODE: [MessageHandler(Filters.text & ~Filters.command, receive_registration_code)],
        },
        fallbacks=[],
    )

    # Add the ConversationHandler to the dispatcher
    dispatcher.add_handler(registration_handler)

    # Start the bot  
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()