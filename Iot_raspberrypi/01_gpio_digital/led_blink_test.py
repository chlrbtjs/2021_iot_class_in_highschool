import RPi.GPIO as GPIO
import time

LED_PIN_r = 4
LED_PIN_y = 5
LED_PIN_g = 6

GPIO.setmode(GPIO.BCM) #BCM pin번호를 따르겠다는 의미
GPIO.setup(LED_PIN_r, GPIO.OUT)
GPIO.setup(LED_PIN_y, GPIO.OUT)
GPIO.setup(LED_PIN_g, GPIO.OUT)

'''
GPIO.output(LED_PIN_g, GPIO.LOW)
GPIO.output(LED_PIN_r, GPIO.LOW)
GPIO.output(LED_PIN_y, GPIO.LOW)
'''

GPIO.output(LED_PIN_r, GPIO.HIGH)
print("led RED on")

time.sleep(2)

GPIO.output(LED_PIN_r, GPIO.LOW)
GPIO.output(LED_PIN_y, GPIO.HIGH)
print("led RED off and led YELLOW on")

time.sleep(2)

GPIO.output(LED_PIN_y, GPIO.LOW)
GPIO.output(LED_PIN_g, GPIO.HIGH)
print("led YELLOW off and led GREEN on")

time.sleep(2)

GPIO.output(LED_PIN_g, GPIO.LOW)
print("led GREEN off")


GPIO.setup(LED_PIN_r, GPIO.IN)
GPIO.setup(LED_PIN_y, GPIO.IN)
GPIO.setup(LED_PIN_g, GPIO.IN)
GPIO.cleanup() #pin 초기화
