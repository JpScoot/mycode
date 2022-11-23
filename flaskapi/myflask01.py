#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask
import random
# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

artist =["2pac", "nirvana", "janet jackson", "billie holiday"]

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/artist")
def hello_world():
   return random.choice(artist)


@app.route("/james")
def two_functions():
    return "testing"


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE

