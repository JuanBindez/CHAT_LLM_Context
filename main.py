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

context = None
chat_history = []
MODEL = "llama3-8b-8192"
VERSION = "1.0.0"

@app.route("/", methods=["GET", "POST"])
def index():
    global context, chat_history

    model = MODEL
    version = VERSION

    if request.method == "POST":

        if "context" in request.form:
 
            context = request.form.get("context")
            chat_history = [{"role": "system", "content": context}]
            return render_template("index.html", chat_history=chat_history, current_context=context, markdown=markdown, model=model, version=version)

        user_input = request.form.get("user_input")

        if context is None:
            return render_template("index.html", chat_history=chat_history, current_context=context, markdown=markdown, error="Please set a context before starting.", model=model, version=version)

        chat_history.append({"role": "user", "content": user_input})


        chat_completion = client.chat.completions.create(
            messages=chat_history,
            model=MODEL,
        )

        model_response = chat_completion.choices[0].message.content
        chat_history.append({"role": "assistant", "content": model_response})

        return render_template("index.html", chat_history=chat_history, current_context=context, markdown=markdown, model=model, version=version)


    return render_template("index.html", chat_history=chat_history, current_context=context, markdown=markdown, model=model, version=version)


if __name__ == "__main__":
    app.run(debug=True)