from flask import Flask, render_template

app = Flask("JobScraper")

@app.route("/") # decorator
def home():
    return render_template("home.html", name="nico")

@app.route("/hello")
def hello():
    return "<h1>Hello!</h1>"

app.run()