import RPi.GPIO as GPIO
import time

LED_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

#pwm 객체 생성
##GPIO>PWM(핀, 주파수(초당 몇회 반복, 여기서는 1초에 50번 반복하도록))
pwm = GPIO.PWM(LED_PIN, 50) #pwm 이 PWM객체의 주소를 가지고 있다.
pwm.start(0) #duty cycle(0~100) 

try:
    for j in range(3):
        for i in range(0, 101, 5):
            pwm.ChangeDutyCycle(i) 
            time.sleep(0.1)
        
        for i in range(100, 1, -5):
            pwm.ChangeDutyCycle(i)
            time.sleep(0.1)

finally:
    pwm.stop()
    GPIO.setup(LED_PIN, GPIO.IN)
    GPIO.cleanup()
    print('cleanup and exit')