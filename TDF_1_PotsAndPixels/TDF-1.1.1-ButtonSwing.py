import time
from adafruit_crickit import crickit
 
# For signal control, we'll chat directly with seesaw, use 'ss' to shorted typing!
ss = crickit.seesaw
 
# Button is pullup, connect to ground to activate
BUTTON_1 = crickit.SIGNAL1  # button #1 connected to signal port 1 & ground

ss.pin_mode(BUTTON_1, ss.INPUT_PULLUP)

crickit.servo_1.set_pulse_width_range(min_pulse=1000, max_pulse=2000)


while True:
    if not ss.digital_read(BUTTON_1):
        print("Button 1 pressed")
        crickit.servo_1.angle = 0      # right

    else:
        print("Button 1 NOT pressed")
        crickit.servo_1.angle = 180      # left

