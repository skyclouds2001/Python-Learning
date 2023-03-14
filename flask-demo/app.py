from flask import Flask, url_for, request
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p style='color: red'>Hello, World!</p>"


@app.route('/user/<username>', methods=['GET', 'POST'])
def show_user_profile(username: str):
    if request.method == 'GET':
        return f'GET : User - {escape(username)}'
    elif request.method == 'POST':
        return f'POST : User - {escape(username)}'


with app.test_request_context():
    print(url_for('/'))
    print(url_for('/user/<username>'))
