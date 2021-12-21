import RPI.GPIO as GPIO
import time

#서보모터는 반드시 50Hz, Duty Cycle 는 1ms~2ms (=-90도~90도)(=5~10), 제조사에 따라 +-0.5ms

SERVO_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(7.5)

try:
    while True:
        val = input('1: 0d, 2: -90d, 3: 90d other: exit > ')
        if val =='1':
            pwm.ChangeDutyCycle(7.5)
        elif val=='2':
            #pwm.ChangeDutyCycle(5)
            pwm.ChangeDutyCycle(2.5)
        elif val == '3':
            #pwm.ChangeDutyCycle(10)
            pwm.ChangeDutyCycle(12.5)
        else:
            break

finally:
    pwm.stop()
    GPIO.setup(SERVO_PIN, GPIO.IN)
    GPIO.cleanup()