from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Hello World!!</h1>"

@app.route("/test")
def test():
    return "<h2>Test!</h2>"