import RPi.GPIO as GPIO
import time

LED = 4
SERVO = 5
segment7 = [8, 9, 10, 11, 12, 13]
inputdata = 0
segmentdata = [[1, 1, 1, 1, 0, 1], [0, 1, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [1, 1, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [1, 0, 1, 0, 1, 1], [1, 0, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0]]

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(SERVO, GPIO.OUT)
for i in range(6):
    GPIO.setup(segment7[i], GPIO.OUT)
    
def segmentoutput(n):
    for i in range(6):
        GPIO.output(segment7[i], segmentdata[i])



pwm = GPIO.PWM(SERVO, 50)
pwm.start(7.5)

try:
    while True:
        val = input('1: door close, 2: door open, 3: led on, 4:led off 0~9: output, other: exit > ')
        if val =='1':
            pwm.ChangeDutyCycle(7.5)
        elif val=='2':
            #pwm.ChangeDutyCycle(5)
            pwm.ChangeDutyCycle(2.5)
        elif val == '3':
            GPIO.output(LED, GPIO.HIGH)
        elif val == '4':
            GPIO.output(LED, GPIO.LOW)
        elif 0 <= val <=9:
            segmentoutput(val)
        else:
            break

finally:
    GPIO.output(LED, GPIO.LOW)
    GPIO.output(SERVO, GPIO.LOW)
    GPIO.setup(LED, GPIO.IN)
    GPIO.setup(SERVO, GPIO.IN)
