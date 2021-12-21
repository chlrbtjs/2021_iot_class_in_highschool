from lcd import drivers
import time
import datetime

now = datetime.datetime.now()
display = drivers.Lcd()

try:
    display.lcd_display_string(now.strftime("%x, %X"));
    while True:
        display.lcd_display_string("** welcome **", 1)
        time.sleep(2)
        display.lcd_display_string("   welcome   ", 1)
        time.sleep(2)
finally:
    print("display clear")
    display.lcd_clear()
