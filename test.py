import os
import openai
from dotenv import load_dotenv
import gradio as gr


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
            print("rate limit reached")
            return "rate limit reached"

        return reply


messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant."},
]


inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot",
             description="Ask anything you want",
             theme="compact").launch(share=True)
