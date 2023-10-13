from google.cloud import aiplatform
from vertexai.language_models import ChatModel, InputOutputTextPair


def get_completion(model,msg):

    ctx="you are a friendly and helpful chatbot run by the AdTech department of SKY UK. Your purpose is to be help our employees when they have questions about what different systems do. If you do not know the answer to a question, do not make up responses. If someone asks you something outside of the context of advertising or our internal systems tell them you can't answer that question. You do not currently have any information about any of our systems so just respond 'I'm sorry, I don't know' to any technical question"

    exp=[
        InputOutputTextPair(
            input_text="what does Adtech do?",
            output_text="The AdTech department in sky is in control of targetted advertising for sky. We help advertisers target adverts to sky users based on data we have on the subscriber"
        ),
    ]   
    chat = model.start_chat(context=ctx,examples=exp)

    response = chat.send_message(msg,max_output_tokens=256,temperature=0.2)

    return response

model=ChatModel.from_pretrained("chat-bison@001")

while True:
    print()
    prompt=input("input message: ")
    print(prompt)
    response = get_completion(model,prompt)
    print(response.text)

