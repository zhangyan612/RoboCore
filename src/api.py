from flask import Flask, render_template
# import aiy.audio

app = Flask(__name__)


@app.route('/')
def index():
    return "<p>hello this is aiy</p>"

@app.route('/control')
def control():
    try:
        return render_template('control.html')
    except Exception as e:
        return str(e)
    
@app.route('/sound/<text>')
def sound(text):
    # aiy.audio.say(text)
    return 'try to make sound ' + text

#record
#camera
#movement

@app.route('/hello')
def hello():
    return 'this is python api runninng'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)