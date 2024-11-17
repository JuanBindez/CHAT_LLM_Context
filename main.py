import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

context = "you are a programmer"


while True:
    user_input = input("You: ")
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": context
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        model="llama3-8b-8192",
    )
    print("Model:", chat_completion.choices[0].message.content)