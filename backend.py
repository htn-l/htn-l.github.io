from flask import Flask, request


app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def hello():
    return "Hello World!"


@app.route('/register', methods=['GET','POST'])
def show_user_profile():
    data = request.form
    print(data)
    user = data["user"]
    password = data["password"]
    # TODO check if user is in db
    # TODO encrypt with sha256 then store to db
    return "HELLOEOIJAJSLFJAOIFJA"

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)