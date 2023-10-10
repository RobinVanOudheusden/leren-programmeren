import pymongo
from accountActivation import *
from telegram import Update
from telegram.ext import CallbackContext

# Connect to MongoDB database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["triplence-telegram-bot"]
mycol1 = mydb["new_email_registrations"]
mycol = mydb["registrations"]

email = input("Email:\n")
mycol1.insert_one({"email": email})
setup_registration(Update, CallbackContext)