from flask import Flask, render_template, request
# from flask_debugtoolbar import DebugToolbarExtention
from stories import story

app = Flask(__name__)
# app.config['SECRET_KEY'] = "secret"

# debug = DebugToolbarExtention(app)

@app.route("/home")
def the_questions():

    prompts = story.prompts

    return render_template("home.html", prompts=prompts)

@app.route("/story")
def view_story():


    text = story.generate(request.args)

    return render_template("story.html", text = text )
