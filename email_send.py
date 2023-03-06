from speak import speak
from take_command import takeCommand
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.getenv('EMAIL')
PASS = os.getenv('PASS')

def sendGmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(EMAIL, PASS)
    server.sendmail(EMAIL, to, content)
    server.close()

def email(person):
    try:
        speak("What should I say?")
        content = takeCommand()    
        sendGmail(person, content)
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("Sorry I am unable send this email")