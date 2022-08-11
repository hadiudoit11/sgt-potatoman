from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)

@application.route("/healthcheck")
def healthcheck():
    status_code = flask.Response(status=200)
    return status_code

@application.route("/")
def hello_world():

    return 'poo poo pee pee'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
