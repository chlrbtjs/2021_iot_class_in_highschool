import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11

DHT_PIN = 4

try:
    while True:
        h, t = Adafruit_DHT.read_retry(sensor, DHT_PIN)

        if h is not None and t is not None:
            print(f'Temperature={t:.1f}*, Humidity={h:.1f}%')#온도를 *로 표시
            #print('T~~%.1f, H~~%.1f' % (t, h)) 프린트 두가지 방식...   ?

        else:
            print('read error')

        time.sleep(0.1)
finally:
    print('bye')
