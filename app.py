from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.wrappers import response
from surveys import surveys

app = Flask(__name__)
app.config["SECRET_KEY"] = "MY-KEY"
debug = DebugToolbarExtension(app)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

#responses = []


@app.route("/")
def home():
    title = surveys["satisfaction"].title
    instructions = surveys["satisfaction"].instructions
    # responses = session.get("answers", [])
    return render_template("home.html", title=title, instructions=instructions)

@app.route("/question/<int:currPage>")
def question(currPage):
    responses = session.get("answers", [])
    if len(surveys["satisfaction"].questions) <= len(responses):
        return redirect("/thank-you")
    if len(responses) != currPage:
        flash("do not try to cheat")
        flash(f"redirected to question {len(responses)}")
        return redirect(f"/question/{len(responses)}")
    question = surveys["satisfaction"].questions[currPage].question
    option1 = surveys["satisfaction"].questions[currPage].choices[0]
    option2 = surveys["satisfaction"].questions[currPage].choices[1]
    return render_template("questions.html",currPage=currPage, question=question, option1=option1, option2=option2)

@app.route("/answer/<int:currPage>", methods=["POST"])
def answer(currPage):
    selected = request.form["selected"]
    responses = session.get("answers", [])
    responses.append(selected)
    session["answers"] = responses
    return redirect(f"/question/{currPage+1}")

@app.route("/thank-you")
def thankYou():
    return render_template("thank-you.html")