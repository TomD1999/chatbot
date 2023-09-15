Humble beginnings for a chatbot app using chat-gpt


dependencies:
using poetry to manage dependencies. run the below from the root of the project
```
poetry install
```

env variables:
Copy the file .env.example as .env (or run `cp .env.example .env`) then replace the value of `CHAT_GPT_KEY` in .env with your token

running the app:
```
poetry run test.py
```

due to security concerns, had to remove the frontend aspect of the app. Will try to fix it when I get the chance. At the moment it just asks one question then returns the response or a rate limit error
