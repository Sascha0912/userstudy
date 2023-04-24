from flask import Flask, render_template, request
import json
import mariadb
from config.config import *
import uuid
import sys

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


@app.route('/usergenerator', methods=['GET', 'POST'])
def usergenerator():
    if request.method == 'POST':
        age = request.form['age']
        affinity = request.form['affinity']
        print("Age " + age + " affinity: " + affinity)
        myuuid = str(uuid.uuid4())
        userid = str(hash(age+affinity+myuuid) % (sys.maxsize + 1) * 2)

        data = {
            'age': age,
            'affinity': affinity,
            'userid': userid
        }

        return render_template('usergenerator.html', data=data, show_results=1)
    elif request.method == 'GET':
        return render_template('usergenerator.html', show_results=0)


@app.route('/userstudy/privacy', methods=['GET', 'POST'])
def privacy():
    if request.method == 'POST':
        userid = request.form['userid']
        print("User ID: "+str(userid))

        conn = mariadb.connect(
            user=conf['user'],
            password=conf['password'],
            host=conf['host'],
            port=conf['port'],
            database=conf['database']
        )
        cur = conn.cursor()

        # *****************************
        # *          TEST             *
        # *****************************
        # cur.execute("SELECT * FROM users")
        # for userid, age, affinity, privacy_set in cur:
        #     print(f"id: {userid}, age: {age}, affinity: {affinity}, privacy: {privacy_set}")
        # *****************************

        try:
            cur.execute("UPDATE users SET privacy=1 WHERE id=?", (userid,))
        except mariadb.Error as e:
            print(f"Error: {e}")
        conn.commit()
        conn.close()

        return render_template('privacy.html')
    elif request.method == 'GET':
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
