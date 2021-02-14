# -*- coding: utf-8 -*-
# sudo -H pip3 install --upgrade luma.oled
# sudo -H pip3 install serial
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import Image, ImageFont, ImageDraw, ImageOps
import time

serial = i2c(port=1, address=0x3C)
# substitute ssd1331(...) or sh1106(...) below if using that device
device = ssd1306(serial)

# font configuration
ttf = '/usr/share/fonts/truetype/04b_03.ttf'

# oled
serial = i2c(port=1, address=0x3c)
device = ssd1306(serial)

font16 = ImageFont.truetype(ttf, 16)
font8 = ImageFont.truetype(ttf, 8)

def main():
    with canvas(device) as drawUpdate:
        drawUpdate.text((30, 40), "Hello World", font=font8, fill=255)
        #drawUpdate.text((1,52), "Waiting internet connection... Make sure Raspberry Pi is connected to internet.. ", font=font8, fill=255)

def update(distance):
    with canvas(device) as drawUpdate:
        drawUpdate.text((0, 0), "Distance".format((distance/ 10.0)) , font=font16, fill=100)
        drawUpdate.text((10, 20), "{:.2f} cm".format((distance/ 10.0)) , font=font16, fill=255)
        drawUpdate.text((10, 40), "{:.2f} c".format( 34.5) , font=font16, fill=255)


def message(text):
    with canvas(device) as drawUpdate:
        drawUpdate.text((0, 20), text , font=font16, fill=255)


#if __name__ == "__main__":
#    main()
#    time.sleep(10)


