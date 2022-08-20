from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "<p>hello this is aiy</p>"

@app.route('/sound/<text>')
def sound(text):
    return 'try to make sound ' + text

#record
#camera
#movement

@app.route('/hello')
def hello():
    return 'this is python api runninng'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)