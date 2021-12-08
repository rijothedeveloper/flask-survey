from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import surveys

app = Flask(__name__)
app.config["SECRET_KEY"] = "MY-KEY"
debug = DebugToolbarExtension(app)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

responses = []

@app.route("/")
def home():
    title = surveys["satisfaction"].title
    instructions = surveys["satisfaction"].instructions
    return render_template("home.html", title=title, instructions=instructions)

@app.route("/question/<int:currPage>")
def question(currPage):
    if len(surveys["satisfaction"].questions) <= currPage:
        return redirect("/thank-you")
    question = surveys["satisfaction"].questions[currPage].question
    option1 = surveys["satisfaction"].questions[currPage].choices[0]
    option2 = surveys["satisfaction"].questions[currPage].choices[1]
    return render_template("questions.html",currPage=currPage, question=question, option1=option1, option2=option2)

@app.route("/answer/<int:currPage>", methods=["POST"])
def answer(currPage):
    selected = request.form["selected"]
    responses.append(selected)
    return redirect(f"/question/{currPage+1}")

@app.route("/thank-you")
def thankYou():
    return render_template("thank-you.html")