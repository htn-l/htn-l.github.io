import json
from flask_cors import CORS
from flask import Flask, request
from hashlib import sha256

app = Flask(__name__)
CORS(app)
success = dict()
success["result"] = "true"

fail = dict()
fail["result"] = "true"


@app.route('/r', methods=['POST'])
def show_user_profile():
    data = request.form
    print(data)
    user = data["username"]
    password = data["password"]
    # TODO check if user is in db
    # if (not in db):
    # return
    # TODO encrypt with sha256 then store to db
    hashedPass = sha256(password.encode()).hexdigest()
    print(hashedPass)
    return json.dumps(success)


@app.route('/signin', methods=['POST'])
def sign_in():
    data = request.form
    print(data)
    user = data["user"]
    password = data["password"]
    # TODO Get users password hashed and compare to the hash
    storedPass = ""
    if storedPass == sha256(bytes(password)).hexdigest():
        return json.dumps(success)


if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
