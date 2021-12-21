import RPi.GPIO as GPIO
import time

piezo_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(piezo_PIN, GPIO.OUT)


melody = [262, 294, 330, 349, 392, 440, 494, 523] #도~도 Hz
#pwm 인스턴스 생성, 도 음은 약 262Hz

try:
    for i in melody:
        pwm.ChangeFrequency(i)
        time.sleep(1)

finally:
    pwm.stop()
    GPIO.setup(piezo_PIN, GPIO.IN)
    GPIO.cleanup()

