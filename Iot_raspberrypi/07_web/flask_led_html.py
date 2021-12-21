from flask import Flask, render_template
import RPi.GPIO as GPIO

LED_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("led.html")

@app.route("/led/<op>")
def led_op(op):
    if op == "on":
        GPIO.output(LED_PIN, GPIO.HIGH)
        return "LED ON"
    elif op == "off":
        GPIO.output(LED_PIN, GPIO.LOW)
        return "LED OFF"
    else :
        return "ERROR"


if __name__ == "__main__": #터미널에서 실행된 경우
    try:
        app.run(host="0.0.0.0")
    finally:
        print("clean up")
        GPIO.output(LED_PIN, GPIO.LOW)
        GPIO.setup(LED_PIN, GPIO.IN)
        GPIO.cleanup()
    