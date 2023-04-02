from flask import Flask, render_template, request
import pyttsx3
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        user_input = request.form["user_input"]
        if user_input == "bye":
            message = "Signing off till then, be happy, be healthy!!!"
            engine = pyttsx3.init()
            engine.say(message)
            engine.runAndWait()
            return render_template("index.html", message=message)
        else:
            message = user_input

            engine = pyttsx3.init()
            engine.say(user_input)
            engine.runAndWait()
            return render_template("index.html", message=message)
    else:
        message = "Enter what you want to say:"
        engine = pyttsx3.init()
        engine.say(message)
        engine.runAndWait()
        return render_template("index.html", message=message)

    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)
