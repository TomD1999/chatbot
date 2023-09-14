Humble beginnings for a chatbot app using chat-gpt


dependencies:
using poetry to manage dependencies. run the below from the root of the project
```
poetry install
```

env variables:
Copy the file .env.example as .env (or run `cp .env.example .env`) then replace the value of `CHAT_GPT_KEY` with your token

running the app:
```
poetry run test.py
```

should be able to access from:  http://127.0.0.1:7860
