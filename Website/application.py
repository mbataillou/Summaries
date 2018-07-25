from flask import Flask, render_template

app = Flask(__name__)
app.debug = True


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/centrale")
def centrale():
    return render_template("centrale.html")

@app.route("/caminos")
def caminos():
    return render_template("caminos.html")

@app.route("/dauphine")
def dauphine():
    return render_template("dauphine.html")

@app.route("/contribute")
def contribute():
    return render_template("contribute.html")

@app.route("/honors")
def honors():
    return render_template("honors.html")
