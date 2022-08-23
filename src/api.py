from flask import Flask, render_template, request, jsonify
# import aiy.audio
import ArduinoController as Arduino

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


@app.route('/servo', methods=['POST'])
def servo():
    data = request.json
    # print(data['command1'])
    # print(data['command2'])
    Arduino.sendCommand(int(data['command1']), int(data['command2']), int(data['command3']), int(data['command4']), int(data['command5']), int(data['command6']))
    return jsonify(data)
    # aiy.audio.say(text)
    # return 'servo moved'

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