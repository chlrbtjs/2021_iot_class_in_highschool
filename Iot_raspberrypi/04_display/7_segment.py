import RPi.GPIO as GPIO
import time

#GPIO 7개 핀 설정
#              A  B  C  D  E  F  G
SEGMANT_PIN = [2, 3, 4, 5, 6, 7, 8]

GPIO.setmode(GPIO.BCM)
for i in SEGMANT_PIN:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)

#common cathode
data = [1, 1, 1, 1, 1, 1, 0]

try:
    for _ in range(3):
        for i in range(7):
            GPIO.output(SEGMANT_PIN[i], data[i])

        time.sleep(1)
        for i in range(7):
            GPIO.output(SEGMANT_PIN[i], GPIO.LOW)
        time.sleep(1)

finally:
    for i in range(7):
        GPIO.setup(SEGMANT_PIN[i], GPIO.IN)
    GPIO.cleanup()
    print("bye")
