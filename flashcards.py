from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to my Flash Cards application!"

@app.route("/date")
def date():
    return "this page was served at " + str(datetime.now())

# if __name__ == '__main__':
#     app.run()