from lcd import drivers
import time

display = drivers.Lcd()

try:
    display.lcd_display_string("Hello, World!!", 1)
    while True:
        display.lcd_display_string("** welcome **", 2)
        time.sleep(2)
        display.lcd_display_string("   welcome   ", 2)
        time.sleep(2)
finally:
    print("display clear")
    display.lcd_clear()
