from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('overview.html')


@app.route('/userstudy/studyu')
def studyu():
    return render_template('studyu.html')


@app.route('/userstudy/1_0')
def study1_0():
    return render_template('userstudy1_0.html')


if __name__ == '__main__':
    app.run()
