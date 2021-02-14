from Adafruit_AMG88xx import Adafruit_AMG88xx
import os
import math
import time
import numpy as np

import oled
from vl53l0x.api import VL53L0X

tof = VL53L0X()
tof.setup()        

os.putenv('SDL_FBDEV', '/dev/fb1')

#initialize the sensor
sensor = Adafruit_AMG88xx()

#some utility functions
def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

def map(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

#let the sensor initialize
time.sleep(.1)
	
while(1):

	distance = tof.measure()
	if(distance == 0):
		oled.message("Too close")
	elif(distance == 8190):
		oled.message("Too far")
	else:
		oled.update(distance)

	#read the pixels
	pixels = sensor.readPixels()
	print(pixels)
	#pixels = [map(p, MINTEMP, MAXTEMP, 0, COLORDEPTH - 1) for p in pixels]
		
	