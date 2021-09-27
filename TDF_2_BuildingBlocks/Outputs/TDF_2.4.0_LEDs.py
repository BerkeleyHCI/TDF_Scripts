import time
from adafruit_crickit import crickit
 
# For signal control, we'll chat directly with seesaw, use 'ss' to shorted typing!
ss = crickit.seesaw

# Two LEDs are outputs, on by default
LED_1 = crickit.SIGNAL5 # LED #1 connected to signal port 5 & ground
LED_2 = crickit.SIGNAL6 # LED #2 connected to signal port 6 & ground
LED_3 = crickit.SIGNAL7 # LED #3 connected to signal port 7 & ground
 
ss.pin_mode(LED_1, ss.OUTPUT)
ss.pin_mode(LED_2, ss.OUTPUT)
ss.pin_mode(LED_3, ss.OUTPUT)

ss.digital_write(LED_1, True)
ss.digital_write(LED_2, True)
ss.digital_write(LED_3, True)
 
while True:
    
    ss.digital_write(LED_1, True)
    ss.digital_write(LED_2, False)
    ss.digital_write(LED_3, False)
    time.sleep(1)

    ss.digital_write(LED_1, False)
    ss.digital_write(LED_2, True)
    ss.digital_write(LED_3, False)
    time.sleep(1)

    ss.digital_write(LED_1, False)
    ss.digital_write(LED_2, False)
    ss.digital_write(LED_3, True)
    time.sleep(1)