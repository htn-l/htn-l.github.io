import json
from flask_cors import CORS
from flask import Flask, request
from hashlib import sha256

app = Flask(__name__)
CORS(app)


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


if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
