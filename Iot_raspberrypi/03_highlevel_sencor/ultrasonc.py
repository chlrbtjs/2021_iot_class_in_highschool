import RPi.GPIO as GPIO
import time

trriger_PIN = 4
echo_PIN = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(trriger_PIN, GPIO.OUt)
GPIO.setup(echo_PIN, GPIO,IN)

try:
    while True:
        GPIO.output(trriger_PIN, GPIO.HIGH)
        time.sleep(0.00001) #10us(마이크로, 1us=0.000001s)
        GPIO.output(trriger_PIN, GPIO.LOW)


        #echoPIN -> HIGH (start time)
        while GPIO.input(echo_PIN) == 0:
            pass
        
        Start = time.time()
        while GPIO.input(echo_PIN) ==1:
            pass
        stop = time.time()

        dt = stop - Start
        dis = 17160 * dt

        print('dis : %.1fcm' % dis)

finally:
    GPIO.setup(trriger_PIN, GPIO.IN)
    GPIO.setup(echo_PIN, GPIO,IN)
    GPIO.cleanup()

    print('clean up and exit')