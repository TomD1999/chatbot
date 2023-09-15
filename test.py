import os
import openai
from dotenv import load_dotenv


load_dotenv()

openai.api_key = os.getenv("CHAT_GPT_KEY")

messages = [
    {"role": "system", "content": "say hi"},
]


def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        try:
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
            )
            reply = chat.choices[0].message.content
            messages.append({"role": "assistant", "content": reply})
        except openai.error.RateLimitError:
            return "rate limit reached"

        return reply


messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant."},
]

print(chatbot("test"))
