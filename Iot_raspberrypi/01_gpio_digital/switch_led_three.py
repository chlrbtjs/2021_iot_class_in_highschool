import RPi.GPIO as GPIO
import time

LED_R = 4
LED_G = 5
LED_Y = 6
SWITCH_R = 12
SWITCH_G = 13
SWITCH_Y = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)
GPIO.setup(LED_Y, GPIO.OUT)
GPIO.setup(SWITCH_R, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(SWITCH_G, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(SWITCH_Y, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

try:
    while True:
        valr = GPIO.input(SWITCH_R)
        valg = GPIO.input(SWITCH_G)
        valy = GPIO.input(SWITCH_Y)
        print(valr, valg, valy)
        GPIO.output(LED_R, valr)
        GPIO.output(LED_G, valg)
        GPIO.output(LED_Y, valy)

        time.sleep(0.1)

finally:
    GPIO.setup(LED_R, GPIO.IN)
    GPIO.setup(LED_G, GPIO.IN)
    GPIO.setup(LED_Y, GPIO.IN)
    GPIO.cleanup()
    print('cleanup and exit')
