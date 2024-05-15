from flask import Flask

app = Flask("JobScrapper")

@app.route("/") # decorator
def home():
    return "hey there!"

app.run()