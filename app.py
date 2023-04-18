from flask import Flask, render_template
import json
import mariadb
from config.config import *

app = Flask(__name__)


def check_user():
    mariadb.connect(
        host=conf['host'],
        port=conf['port'],
        user=conf['user'],
        password=conf['password'],
        database=conf['database']
    )


@app.route('/')
def hello_world():  # put application's code here
    # check_user()
    return render_template('overview.html')


@app.route('/userstudy/privacy')
def privacy():
    return render_template('privacy.html')


@app.route('/userstudy/studyu')
def studyu():
    return render_template('studyu.html')


@app.route('/userstudy/1_0')
def study1_0():
    return render_template('userstudy1_0.html')


@app.route('/userstudy/2_0')
def study2_0():
    return render_template('userstudy2_0.html')


@app.route('/userstudy/3_0')
def study3_0():
    return render_template('userstudy3_0.html')


@app.route('/userstudy/4_0')
def study4_0():
    return render_template('userstudy4_0.html')


@app.route('/userstudy/5_0')
def study5_0():
    return render_template('userstudy5_0.html')


if __name__ == '__main__':
    app.run()
