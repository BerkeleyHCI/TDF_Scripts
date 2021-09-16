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


def translate(value, leftMin, leftMax, rightMin, rightMax): #Attributed to Adam Luchjenbroers, 12/8/2009
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)


# main function:

while True:
    potValue = ss.analog_read(pot) # read the pot pin and set that reading to our potValue variable

# this code re-maps our pot value (0 - 1023) to whatever range we want, even negative ranges:
    potValueAdjusted = translate(potValue, 10, 1023, 0, 2000)

    print("Pot value ", potValue, " has been adjusted to ", round(potValueAdjusted)) # print that value for our information
# this is where you use that adjusted potentiometer value to control other things



    time.sleep(0.25) # wait .25 seconds to slow down the interaction