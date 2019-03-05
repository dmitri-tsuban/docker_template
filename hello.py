from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print(1+2)
    return "Hello, my friend!"