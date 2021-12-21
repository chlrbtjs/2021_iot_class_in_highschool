import RPi.GPIO as GPIO
import time

PIR_PIN = 4
led_PIN = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(led_PIN, GPIO.OUt)

time.sleep(5)
print('RPI ready......')

try:
    while True:
        val = GPIO.input(PIR_PIN)

        if val == 1:
            GPIO.output(led_PIN, GPIO.HIGH)
            print('움직임 감지, led on')
        else:
            GPIO.output(led_PIN, GPIO.LOW)
            print('움직임 없음, led off')

        time.sleep(0.1)
    
finally:
    GPIO.setup(led_PIN, GPIO.IN)
    GPIO.cleanup()
    print('cleanup and exit')
    