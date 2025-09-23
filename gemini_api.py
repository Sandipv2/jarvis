#----------- Core modules ---------
import os

#----------- External modules ---------
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

chat_history = "You are Jarvis - The most friendly AI Assistant. Give brief and concise responses, not detailed one. Provide detailed resposes only when asked. And don't put 'Jarvis:' before response."


def chat(prompt):
    global chat_history
    chat_history += f'User: {prompt}\n Jarvis: '
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=chat_history
        )
        
        chat_history += f'{response.text}\n'
        return response.text
    
    except Exception as e:
        return f'Error while generating res: {e}'