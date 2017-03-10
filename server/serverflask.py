from flask import Flask
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

@app.route("/")

def hello():
    return "Welcome to Python Flask App!"

if __name__ == "__main__":
    app.run()