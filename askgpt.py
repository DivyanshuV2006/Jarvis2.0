import openai
from dotenv import load_dotenv
import os
from speak import speak

load_dotenv()
GPT = os.getenv("GPT")

def askGPT(text):
    openai.api_key = GPT
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = text,
        temperature = 0.6,
        max_tokens = 2050,
    )
    return speak(response.choices[0].text)
    #return print(response.choices[0].text)