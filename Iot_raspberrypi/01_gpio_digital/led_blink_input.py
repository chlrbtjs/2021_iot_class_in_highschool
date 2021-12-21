import RPi.GPIO as GPIO

LED_PIN = 4
GPIO.setmode(GPIO.BCM) #BCM pin번호를 따르겠다는 의미
GPIO.setup(LED_PIN, GPIO.OUT)

'''
GPIO.output(LED_PIN_g, GPIO.LOW)
GPIO.output(LED_PIN_r, GPIO.LOW)
GPIO.output(LED_PIN_y, GPIO.LOW)
'''

try: 
    while True:
        n=input("0:off, 1:on, other:exit > ")

        if n=='1':
            GPIO.output(LED_PIN, GPIO.HIGH)
            print("led on")
        elif n=='0':
            GPIO.output(LED_PIN, GPIO.LOW)
            print("led off")
        else:
            print("exit")
            break

finally:
    print("clean up")
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.setup(LED_PIN, GPIO.IN)
    GPIO.cleanup() #pin 초기화
