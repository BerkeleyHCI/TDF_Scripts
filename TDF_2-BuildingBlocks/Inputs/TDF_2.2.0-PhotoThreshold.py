# from https://learn.adafruit.com/adafruit-crickit-creative-robotic-interactive-construction-kit/circuitpython-signals
# accessed 02012021

# libraries
import time
from adafruit_crickit import crickit
 
# For signal control, we'll chat directly with seesaw, use 'ss' to shorted typing!
ss = crickit.seesaw

# potentiometer connected to signal #2
LDR = crickit.SIGNAL8

# establish the pin mode of our variable "pot" as input
ss.pin_mode(LDR, ss.INPUT)

# establish other variables
lowerThreshold = 800
higherThreshold = 900

# main function:

while True:
    LDRValue = ss.analog_read(LDR) # read the LDR pin and set that reading to our LDRValue variable
    print(LDRValue) # print that value for our information

    if (LDRValue > higherThreshold):
      # this is where you specify what happens at a higher threshold
        print("Higher threshold exceeded")
      # this is where you specify what happens when you exceed a high threshold
    
    elif (LDRValue > lowerThreshold):
        print("Lower threshold exceeded")
      # this is where you specify what happens when you exceed a low threshold

    else:
        print("Below lower threshold")
      # this is where you specify what happens when you're below both thresholds
      
    time.sleep(0.25) # wait .25 seconds to slow down the interaction
