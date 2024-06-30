# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, jsonify, request
import random

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'

jokes = [
    "My boss said “dress for the job you want, not for the job you have.” So I went in as Batman.",
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Have you ever heard about the kidnapping at school? It's okay, he woke up.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "What do you get when you cross a snowman and a vampire? Frostbite.",
    "I'm not a fan of spring cleaning. Let's be honest, I'm not into summer, fall, or winter cleaning either.",
    "Why was the math book sad? Because it had too many problems.",
    "What do you call fake spaghetti? An impasta!",
    "Why was the broom late? It swept in.",
    "I was going to tell you a joke about boxing but I forgot the punch line.",
    "Why don't some couples go to the gym? Because some relationships don't work out.",
    "My uncle named his dogs Timex and Rolex. They're his watch dogs.",
    "What do you call a fish with no eyes? Fsh.",
    "What do you get when you put a vest on an alligator? An investigator."
]

@app.route('/random-joke', methods=['GET'])
def get_random_joke():
    # joke = random.choice(jokes)
    num = request.args.get('num', default=1, type=int)
    if num < 1:
        return jsonify({"error": "Number of jokes must be at least 1"}), 400

    random_jokes = random.sample(jokes, min(num, len(jokes)))

    return jsonify(random_jokes)


    # return jsonify({'Here is your random joke': joke})

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
