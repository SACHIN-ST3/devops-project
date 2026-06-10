from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "return Version 3 Auto Deploy by Jenkins"

app.run(host='0.0.0.0', port=5000)