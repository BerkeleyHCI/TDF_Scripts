#from https://learn.adafruit.com/adafruit-crickit-creative-robotic-interactive-construction-kit/circuitpython-signals
#accessed 02012021

import time
from adafruit_crickit import crickit
 
# For signal control, we'll chat directly with seesaw, use 'ss' to shorted typing!
ss = crickit.seesaw
# potentiometer connected to signal #3
pot = crickit.SIGNAL2

ss.pin_mode(pot, ss.INPUT)

while True:
    potValue = ss.analog_read(pot)
    print((potValue))

    time.sleep(0.25)
