import openai
import requests
import json
from dotenv import load_dotenv
import os

def maveli(text):
    api_key=''
    if(api_key==''):
        return "Input API key"
    openai.api_key = api_key
    URL = "https://api.openai.com/v1/chat/completions"
    
    payload = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "reply as you are mahabali.someone  asks like this:"+text}],
    "temperature" : 1.0,
    "top_p":1.0,
    "n" : 1,
    "stream": False,
    "presence_penalty":0,
    "frequency_penalty":0,
    }

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai.api_key}"
    }

    response = requests.post(URL, headers=headers, json=payload, stream=False)

    data=json.loads(response.content)
    
    summary = data['choices'][0]['message']['content']
    return summary
