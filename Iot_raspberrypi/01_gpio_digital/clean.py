import RPi.GPIO as GPIO

LED_PIN_r = 4
LED_PIN_y = 5
LED_PIN_g = 6

GPIO.setmode(GPIO.BCM) #BCM pin번호를 따르겠다는 의미
GPIO.setup(LED_PIN_r, GPIO.OUT)
GPIO.setup(LED_PIN_y, GPIO.OUT)
GPIO.setup(LED_PIN_g, GPIO.OUT)

GPIO.cleanup() #pin 초기화
