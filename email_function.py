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