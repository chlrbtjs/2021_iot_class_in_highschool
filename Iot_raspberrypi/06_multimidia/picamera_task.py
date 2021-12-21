import picamera
import time

path = '/home/pi/src4/Iot_raspberrypi/06_multimidia/task'

camera = picamera.PiCamera()

try:
    camera.resolution = (640, 480)
    camera.start_preview()
    time.sleep(3) #딜레이 필요
    while True:
        inputdata = int(input("photo: 1, vidio: 2, exit: 9 > "))
        now_str = time.strftime("%Y%m%d_%H%M%S")

        if inputdata == 1:
            camera.capture('%s/photo_%s.jpg' % (path, now_str))
        elif inputdata == 2:
            camera.start_recording('%s/vidio_%s.h264' % (path, now_str))
            input()
            camera.stop_recording()
        elif inputdata == 9:
            break
        else:
            print("incorrect command")

finally:
    camera.stop_preview()
