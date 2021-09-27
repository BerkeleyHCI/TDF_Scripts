# from https://learn.adafruit.com/adafruit-crickit-creative-robotic-interactive-construction-kit/circuitpython-signals
# accessed 02012021

# libraries
import time
from adafruit_crickit import crickit
 
# For signal control, we'll chat directly with seesaw, use 'ss' to shorted typing!
ss = crickit.seesaw

# potentiometer connected to signal #2
pot = crickit.SIGNAL2

# establish the pin mode of our variable "pot" as input
ss.pin_mode(pot, ss.INPUT)

# main function:

while True:
    potValue = ss.analog_read(pot) # read the pot pin and set that reading to our potValue variable
    print(potValue) # print that value for our information

    if (potValue > threshold):
      # this is where you specify what happens

    else:
      # this is where you specify what happens otherwise

    time.sleep(0.25) # wait .25 seconds to slow down the interaction