from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import surveys

app = Flask(__name__)
app.config["SECRET_KEY"] = "MY-KEY"
debug = DebugToolbarExtension(app)


responses = []

@app.route("/")
def home():
    title = surveys["satisfaction"].title
    instructions = surveys["satisfaction"].instructions
    return render_template("home.html", title=title, instructions=instructions)