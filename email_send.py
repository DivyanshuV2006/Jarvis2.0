from email_function import sendGmail
from speak import speak
from take_command import takeCommand

def email(person):
    try:
        speak("What should I say?")
        content = takeCommand()    
        sendGmail(person, content)
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("Sorry I am unable send this email")