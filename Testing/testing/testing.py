import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import string

mail_to_address = input("Enter the email adress you want to registrate on: \n")

for i in range(1):
    #App-Password code dijc uzfw goww qvhw
    my_adress = 'robin.supraenet@gmail.com'
    password = 'dijc uzfw goww qvhw'

    password_characters = string.digits
    # Generate 10 character long password by random and return it
    password_characters = ''.join(random.choice(password_characters) for i in range(9))

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(my_adress, password)

    msg = MIMEMultipart()  # create a message

    # add in the actual person name to the message template
    message = "Dit is een test e-mail.\n" \
              "Met dit account kunt u in de telegram app communiceren met de bot: Supraenet_Telegram_Bot\n" \
              "Uw activatie code: " + password_characters + "\n" \
              "Met vriendelijke groet,\n\n" \
              "Robin van Oudheusden\n" \
              "Triplence Technologies"
    # Prints out the message body for our sake

    # setup the parameters of the message
    msg['From'] = my_adress
    msg['To'] = mail_to_address
    msg['Subject'] = "Aanmelding Triplence Telegram bot"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    s.send_message(msg)
    del msg

    # Terminate the SMTP session and close the connection
    s.quit()

    print("Email sent to: " + mail_to_address + "\n")
    registration = input("Enter the registration code you received by email: \n")
    if registration == password_characters:
        print("Registration code is correct!\n")
        break
    
