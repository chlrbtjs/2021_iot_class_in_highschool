import picamera
import time

path = '/home/pi/src4/Iot_raspberrypi/06_multimidia'

camera = picamera.PiCamera()

try:
    camera.resolution = (640, 480)
    camera.start_preview()
    time.sleep(3) #딜레이 필요
    camera.capture('%s/photo.jpg' % path) #사진 찍음(저장)

finally:
    camera.stop_preview()
