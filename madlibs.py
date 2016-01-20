from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

MADLIBS = ['madlib.html', 'madlib2.html', 'madlib3.html']

@app.route('/')
def start_here():
    """Homepage."""

    return """<html>
                <body>

                  <h1>Go to hello</h1>
                  <a href="http://127.0.0.1:5000/hello">link here!</a>
                </body>

              </html>"""




@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player= request.args.get("person")
    print player 

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_game_form():
    """Asking user if they want to play a game"""

    player= request.args.get("play")
    print request.args 
    # person= request.args.get("person")

    # print person 
    if player == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")

@app.route('/madlib')
def show_madlib():

    person= request.args.get("person")
    color= request.args.get("color")
    foods= request.args.getlist("food")
    adjective= request.args.get("adjective")

    # print noun
    # random_ml = choice(MADLIBS)


    return render_template(choice(MADLIBS),
                           foods=foods,
                           color=color,
                           person=person,
                           adjective=adjective)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
