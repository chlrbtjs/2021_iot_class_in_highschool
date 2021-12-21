import spidev
import time
import RPi.GPIO as GPIO

LED = 4

GPIO.setmode(GPIO.BCM) #BCM pin번호를 따르겠다는 의미
GPIO.setup(LED, GPIO.OUT)

spi = spidev.SpiDev()

spi.open(0, 0)


spi.max_speed_hz = 100000


def analog_read(channel):

    ret = spi.xfer2([1, (8+channel) << 4, 0]) 
    print(ret)
    adc_out = ((ret[1] & 3) << 8) + ret[2]
    return adc_out

try:
    while True:
        reading = analog_read(0)
        if reading < 512:
            GPIO.output(LED, GPIO.HIGH)
        else:
            GPIO.output(LED, GPIO.LOW)
        print(reading)
        time.sleep(0.5)
finally:
    GPIO.output(LED, GPIO.LOW)
    GPIO.setup(LED, GPIO.IN)
    spi.close()
