##from __future__ import absolute_import
##from __future__ import division, print_function, unicode_literals
##import json
##from flask_cors import CORS
##from flask import Flask, request
##from flask import render_template
##from hashlib import sha256
##
##app = Flask(__name__)
##CORS(app)
##
##def get_summary(text):
##
##    from sumy.parsers.html import HtmlParser
##    from sumy.parsers.plaintext import PlaintextParser
##    from sumy.nlp.tokenizers import Tokenizer
##    from sumy.summarizers.lsa import LsaSummarizer as Summarizer
##    from sumy.nlp.stemmers import Stemmer
##    from sumy.utils import get_stop_words
##
##
##    LANGUAGE = "english"
##    SENTENCES_COUNT = 2
##
##    parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))
##    stemmer = Stemmer(LANGUAGE)
##
##    summarizer = Summarizer(stemmer)
##    summarizer.stop_words = get_stop_words(LANGUAGE)
##
##    for sentence in summarizer(parser.document, SENTENCES_COUNT):
##        print(sentence)
##
##@app.route('/')
##def home():
##    #console.log("h")
##    print("h")
##    return render_template("login.html", name=None)
##
##@app.route('/r', methods=['POST'])
##def show_user_profile():
##    data = request.form
##    print(data)
##    user = data["username"]
##    password = data["password"]
##    # TODO check if user is in db if not create otherwise sign in
##    # if (not in db):
##    # return
##    hashedPass = sha256(password.encode()).hexdigest()
##    print(hashedPass)
##    success = dict()
##    success["result"] = "200"
##    return json.dumps(success)
##
##
##@app.route('/signin', methods=['POST'])
##def sign_in():
##    data = request.form
##    print(data)
##    user = data["user"]
##    password = data["password"]
##    # TODO Get users password hashed and compare to the hash
##    storedPass = "043a718774c572bd8a25adbeb1bfcd5c0256ae11cecf9f9c3f925d0e52beaf89"
##    if storedPass == sha256(bytes(password)).hexdigest():
##        success = dict()
##        success["result"] = "200"
##        return json.dumps(success)
##    else:
##        fail = dict()
##        fail["result"] = "403"
##        return json.dumps(fail)
##
##
##if __name__ == '__main__':
##    app.run(use_reloader=True, debug=True)






















from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
import json
from flask_cors import CORS
from flask import Flask, request
from flask import render_template
from hashlib import sha256

app = Flask(__name__)
CORS(app)

def get_summary(text):

    from sumy.parsers.html import HtmlParser
    from sumy.parsers.plaintext import PlaintextParser
    from sumy.nlp.tokenizers import Tokenizer
    from sumy.summarizers.lsa import LsaSummarizer as Summarizer
    from sumy.nlp.stemmers import Stemmer
    from sumy.utils import get_stop_words


    LANGUAGE = "english"
    SENTENCES_COUNT = 2

    parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)


@app.route("/transcript", methods=["POST"])
def get_summaryi():
    data = request.form
    print(data)
    text = data["text"]
    summary = get_summary(text)
    success = dict()
    success["result"] = summary
    return json.dumps(success)

@app.route('/r', methods=['POST'])
def show_user_profile():
    data = request.form
    print(data)
    user = data["username"]
    password = data["password"]
    # TODO check if user is in db if not create otherwise sign in
    # if (not in db):
    # return
    hashedPass = sha256(password.encode()).hexdigest()
    print(hashedPass)
    success = dict()
    success["result"] = "200"
    return json.dumps(success)


@app.route('/signin', methods=['POST'])
def sign_in():
    data = request.form
    print(data)
    user = data["user"]
    password = data["password"]
    # TODO Get users password hashed and compare to the hash
    storedPass = "043a718774c572bd8a25adbeb1bfcd5c0256ae11cecf9f9c3f925d0e52beaf89"
    if storedPass == sha256(bytes(password)).hexdigest():
        success = dict()
        success["result"] = "200"
        return json.dumps(success)
    else:
        fail = dict()
        fail["result"] = "403"
        return json.dumps(fail)

@app.route('/')
def home():
    #console.log("h")
    print("h")
    return render_template("login.html", name=None)
if __name__ == '__main__':
    s = get_summary("""Prime Minister Justin Trudeau will help open the Hack the North conference at the University of Waterloo Friday night

    Trudeau is scheduled to be part of the opening ceremonies and speak to the crowd at 8:30 pm

    Hack the North brings more than 1,000 students from around the globe to the University of Waterloo campus for a 36 hour hack-a-thon

    Pokemon Go similar to game students created at UW competition in 2014
    Health hack-a-thon in Kitchener to tackle problems faced by aging population
    After the opening remarks by Trudeau there will be a fireside chat with Balaji Srinivasan, CEO of the website 21co, which allows people to be paid with digital currency for doing small tasks, and Mike Gibson, an investor with the San Francisco-based 1517 Fund They're expected to talk about the future of technology in Canada, Silicon Valley and beyond

    The event will also include a panel on diversity and inclusion in the tech sector

    The students will design hardware projects or mobile or web applications during the weekend and present them to a panel of industry experts Sunday morning The top 14 teams will then present to an audience at 2 pm and compete for prizes


    """)
    print("a")
    app.run(use_reloader=True, debug=True)
    print("b")

