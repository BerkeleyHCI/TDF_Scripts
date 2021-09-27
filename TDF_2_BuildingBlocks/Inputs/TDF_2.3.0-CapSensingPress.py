# from https://learn.adafruit.com/adafruit-crickit-hat-for-raspberry-pi-linux-computers?view=all#recommended-capacitive-touch

import time
from adafruit_crickit import crickit
 
# Capacitive touch tests
 
while True:
    if crickit.touch_1.value:
        print("Touched Cap Touch Pad 1")
    if crickit.touch_2.value:
        print("Touched Cap Touch Pad 2")
    if crickit.touch_3.value:
        print("Touched Cap Touch Pad 3")
    if crickit.touch_4.value:
        print("Touched Cap Touch Pad 4")