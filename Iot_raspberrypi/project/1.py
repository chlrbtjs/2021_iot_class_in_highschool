# OLED 조정 라이브러리
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
from board import SCL, SDA
import adafruit_ssd1306

import time

OLED_DISPLAY = 0x3c

RESET_PIN = digitalio.DigitalInOut(board.D4)

i2c = board.I2C()

oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=OLED_DISPLAY, reset=RESET_PIN)

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)

oled.fill(0)
oled.show()