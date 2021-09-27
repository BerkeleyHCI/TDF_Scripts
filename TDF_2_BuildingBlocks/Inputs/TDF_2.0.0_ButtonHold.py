import time
from adafruit_crickit import crickit
 
# For signal control, we'll chat directly with seesaw, use 'ss' to shorted typing!
ss = crickit.seesaw
 
# Button is pullup, connect to ground to activate
BUTTON_1 = crickit.SIGNAL1  # button #1 connected to signal port 1 & ground

ss.pin_mode(BUTTON_1, ss.INPUT_PULLUP)
 
while True:
    if not ss.digital_read(BUTTON_1):
        print("Button 1 pressed")
	# In here, code whatever action you want to happen when button 1 is held



    else:
        print("Button 1 NOT pressed")
	# In here, code whatever action you want to happen when button 1 is not held
