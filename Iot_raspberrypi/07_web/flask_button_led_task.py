from flask import Flask, render_template
import RPi.GPIO as GPIO

G = 4
B = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("button_led_2.html")

@app.route("/<color>/<op>")
def led(color, op):
    if color == 'g':
        if op == '1':
            GPIO.output(G, GPIO.HIGH)
            return "GREEN ON"
        else:
            GPIO.output(G, GPIO.LOW)
            return "GREEN OFF"
    else:
        if op == '1':
            GPIO.output(B, GPIO.HIGH)
            return "BLUE ON"
        else:
            GPIO.output(B, GPIO.LOW)
            return "BLUE OFF"


if __name__ == "__main__": #터미널에서 실행된 경우
    try:
        app.run(host="0.0.0.0")
    finally:
        print("clean up")
        GPIO.output(G, GPIO.LOW)
        GPIO.setup(B, GPIO.IN)
        GPIO.cleanup()