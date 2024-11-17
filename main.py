from flask import Flask, render_template, request
from groq import Groq
from dotenv import load_dotenv
import os
import markdown

load_dotenv()

app = Flask(__name__)

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

context = "programmer"
chat_history = [{"role": "system", "content": context}]


@app.route("/", methods=["GET", "POST"])
def index():
    global chat_history

    if request.method == "POST":
        user_input = request.form.get("user_input")
        
        chat_history.append({"role": "user", "content": user_input})

        chat_completion = client.chat.completions.create(
            messages=chat_history,
            model="llama3-8b-8192",
        )

        model_response = chat_completion.choices[0].message.content

        chat_history.append({"role": "assistant", "content": model_response})

        return render_template("index.html", chat_history=chat_history, markdown=markdown)

    return render_template("index.html", chat_history=chat_history, markdown=markdown)


if __name__ == "__main__":
    app.run(debug=True)
