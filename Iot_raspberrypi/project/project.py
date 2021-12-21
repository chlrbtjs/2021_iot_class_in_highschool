import RPi.GPIO as GPIO
import time

LED = 4
SERVO = 5
segment7 = [17, 27, 22, 6, 13, 19, 26]
segmentdata = [[1, 1, 1, 1, 1, 0, 1], [0, 1, 1, 0, 0, 0, 0], [1, 1, 0, 1, 1, 1, 0], [1, 1, 1, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0]]
#PIN, segment제어를 위한 배열선언

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(SERVO, GPIO.OUT)
for i in segment7:
    GPIO.setup(i, GPIO.OUT)
#setmode, setup
    
def segmentoutput(n):
    for i in range(7):
        GPIO.output(segment7[i], segmentdata[n][i])
#7segment로 n(한자릿수)을 출력하는 함수

pwm = GPIO.PWM(SERVO, 50)
pwm.start(7.5)
#SERVO pwm 시작

try:
    while True:
        val = input('1: door close, 2: door open, 3: led on, 4:led off 0~9: output, other: exit > ')
        segmentoutput(10)
        if val =='1':
            pwm.ChangeDutyCycle(7.5)
        elif val=='2':
            #pwm.ChangeDutyCycle(5)
            pwm.ChangeDutyCycle(2.5)
        elif val == '3':
            GPIO.output(LED, GPIO.HIGH)
        elif val == '4':
            GPIO.output(LED, GPIO.LOW)
        #val을 입력받아 1이면 문(서보모터)을 닫음
        #2이면 문(서보모터)을 염
        #3, 4는 전등 on/off

        if 0 <= int(val) <= 9:
            segmentoutput(int(val))
        else:
            break
        #0~9를 입력받으면 7segment로 출력
        #이외의 수를 입력받으면 프로그램 종료

finally:
    pwm.ChangeDutyCycle(7.5) #종료시 문 닫음
    time.sleep(1) #문(서보모터)이 닫히길 기다림
    GPIO.output(LED, GPIO.LOW)
    GPIO.output(SERVO, GPIO.LOW)
    GPIO.setup(LED, GPIO.IN)
    GPIO.setup(SERVO, GPIO.IN)
    for i in segment7:
        GPIO.output(i, GPIO.LOW)
        GPIO.setup(i, GPIO.IN)
    #PIN이 HIGH인 상태에서 종료되는것을 대비
    #cleanup이 잘 되지 않을때가 있어 직접 IN으로 바꿔줌
    GPIO.cleanup()
    print("bye")
