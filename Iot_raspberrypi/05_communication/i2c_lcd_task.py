from lcd import drivers
import Adafruit_DHT
import time
import datetime

display = drivers.Lcd()

sensor = Adafruit_DHT.DHT11

DHT_PIN = 4

try:

    while True:
        now = datetime.datetime.now()

        print(now.strftime("%x %X"))

        h, t = Adafruit_DHT.read_retry(sensor, DHT_PIN)

        a = now.strftime("%x, %X")

        display.lcd_display_string(f'{a[:9]} {t:.1f}*C', 1)

        if h is not None and t is not None:
            print(f'Temperature={t:.1f}*, Humidity={h:.1f}%')#온도를 *로 표시
            #print('T~~%.1f, H~~%.1f' % (t, h)) 프린트 두가지 방식...   ?

            display.lcd_display_string(f'{a[10:]}, {h:.1f}%', 2)

        else:
            print('read error')

        time.sleep(1)
    
finally:
    print("display clear")
    display.lcd_clear()
