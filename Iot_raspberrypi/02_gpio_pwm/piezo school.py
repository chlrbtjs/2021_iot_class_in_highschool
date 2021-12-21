import RPi.GPIO as GPIO
import time

piezo_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(piezo_PIN, GPIO.OUT)

pwm = GPIO.PWM(piezo_PIN, 1)
pwm.start(10)

melody = [1, 262, 294, 330, 349, 392, 440, 494, 523] #도~도 Hz
#pwm 인스턴스 생성, 도 음은 약 262Hz
school13 = [5, 5, 6, 6, 5, 5, 3, 3]
school2 = [5, 5, 3, 3, 2, 2, 2, 0]
school4 = [5, 3, 2, 3, 1, 1, 1, 0]

try:
    for i in school13:
        pwm.ChangeFrequency(melody[i])
        time.sleep(0.5)
    for i in school2:
        pwm.ChangeFrequency(melody[i])
        time.sleep(0.5)
    for i in school4:
        pwm.ChangeFrequency(melody[i])
        time.sleep(0.5)

finally:
    pwm.stop()
    GPIO.setup(piezo_PIN, GPIO.IN)
    GPIO.cleanup()

