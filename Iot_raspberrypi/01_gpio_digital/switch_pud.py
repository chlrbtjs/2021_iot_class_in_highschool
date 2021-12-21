import RPi.GPIO as GPIO
import time

SWITCH_PIN = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP) #내부 pull_up저항 사용하기
#GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #내부 pull_down저항 사용하기

try:
    while True:
        val = GPIO.input(SWITCH_PIN)
        print(val)
        time.sleep(0.1)

finally:
    GPIO.cleanup()
    print('cleanup and exit')

    
