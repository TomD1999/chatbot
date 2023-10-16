Humble beginnings for a chatbot app using chat-gpt


dependencies:
using poetry to manage dependencies. run the below from the root of the project
```
poetry install
```

GOOGLE PALM2 VERSION:

To run the project:
```
poetry run python3 google_chatbot/chatbot.py
```
need to have gcloud set to a project with vertexAI enabled

DATA: 
example data to be put into the `google_chatbot/examples.py` file in the format there (I didn't want to commit that for security reasons)

OLD VERSION BELOW (CHATGPT VERISION):

env variables:
Copy the file .env.example as .env (or run `cp .env.example .env`) then replace the value of `CHAT_GPT_KEY` in .env with your token

running the chatGPT app (not the main one):
```
poetry run chatbot/gpt_chatbot.py
```

due to security concerns, had to remove the frontend aspect of the app. Will try to fix it when I get the chance. At the moment it just asks one question then returns the response (mostly a rate limit error)

training llm:
```
poetry run train_data.py
```

Lots of these require gpt credits that I don't have, but gives an example of what can be done

