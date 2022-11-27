#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask
from flask import redirect
import random
from flask import jsonify
from flask import request

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

#create a list of quotes
quotes = ["I've missed more than 9000 shots in my career. I've lost almost 300 games. 26 times, I've been trusted to take the game winning shot and missed. I've failed over and over and over again in my life. And that is why I succeed.", "Some people want it to happen, some wish it would happen, others make it happen.", "I can accept failure, everyone fails at something. But I can't accept not trying.", "You can practice shooting eight hours a day, but if your technique is wrong, then all you become is very good at shooting the wrong way. Get the fundamentals down and the level of everything you do will rise."]

#create michael jordan's bio
bio = [{"name": "Michael Jordan", "nickname": "Michael Air Jordan", "birhtday": "Feb, 17, 1963"}]

#create michael jordan historic games
games = ["The Double Nickel Game, In his fifth basketball game back after retiring for 18 months, Michael Jordan scored 55 in a road win against the Knicks in MSG. Michael Jordan always put on a show in New York, and this time was no different. This is easily a must-watch as one of his best performances in The Garden.", 
        "‘The Shot’ Game. Next up on our list of the best Michael Jordan games is ‘The Shot’ game. With the Bull’s tied 2-2 with the Cleveland Cavaliers in the first round of the ‘89 playoffs, Jordan did what he does best. MJ hit plenty of game-winners during his career, and it’s definitely one of our favorites.", 
        "The Flu Game. Michael Jordan faced many challenges in his career, including the flu during the 1997 NBA Finals. In a must-win basketball game, the Bulls faced the Utah Jazz on the road with the series tied 2-2. Jordan shows he can’t lose mentality in this gutsy victory.", 
        "’93 NBA Finals Game 6. We covered this one in our favorite highlights games from Chicago sports history, and there’s a good reason for it. With the team pursuing their first three-peat, Michael Jordan scores a game-high 33 points in the nail-biter against the Suns." ]

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function

#return list (guotes)
@app.route("/michaeljordan")
def michael_jordan_quotes():
   return jsonify(quotes)

#return list (bio)
@app.route("/michaeljordanbio")
def michael_jordan_bio():
    return jsonify(bio)

#return random games
@app.route("/michaeljordangames")
def michael_jordan_games():
    return random.choice(games)

#utilize jinja2
@app.route("/success/<name>")
def james_paul(name):
   # return render_template("postmaker.html")
   return f"Welcome {name}\n"


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE

