from flask import Flask
import RPi.GPIO as GPIO

LED_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

app = Flask(__name__)


@app.route("/")
def hello():
    return '''
        <p>Hello, Flask!</p>
        <a href="/led/red/on">red On</a>
        <a href="/led/red/off">red Off</a> <br>
        <a href="/led/blue/on">blue on</a>
        <a href="/led/blue/off">blue off</a>
    '''

@app.route("/led/<color>/<op>")
def led_op(color, op):
    if color == 'red':
        LED_PIN = 4
    elif color == 'blue':
        LED_PIN = 17
    
    if op == 'on':
        GPIO.output(LED_PIN, GPIO.HIGH)
        return '''
            <p>Led On</p>
            <a href="/">Go Home</a>
        '''
    elif op == 'off':
        GPIO.output(LED_PIN, GPIO.LOW)
        return '''
            <p>Led off</p>
            <a href="/">Go Home</a>
        '''
        



if __name__ == "__main__": #터미널에서 실행된 경우
    try:
        app.run(host="0.0.0.0")
    finally:
        print("clean up")
        GPIO.output(4, GPIO.LOW)
        GPIO.setup(4, GPIO.IN)
        GPIO.output(17, GPIO.LOW)
        GPIO.setup(17, GPIO.IN)
        GPIO.cleanup()
    