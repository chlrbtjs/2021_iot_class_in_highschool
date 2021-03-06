from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.legacy import show_massage
from luma.core.legacy.font import proportional, LCD_FONT

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=1, block_orientation=0, rotate=0, block_arranged_in_reverse_order=False)
print("Created device")

msg = "aaa"
print(msg)
show_massage(device, msg, fill="white", font=proportional(LCD_FONT), scroll_delay=0.1)