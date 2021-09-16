import time
from adafruit_crickit import crickit
 
ss = crickit.seesaw
pot = crickit.SIGNAL2

ss.pin_mode(pot, ss.INPUT)

def translate(value, leftMin, leftMax, rightMin, rightMax): #Adam Luchjenbroers, 12/8/2009
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

while True:
    potValue = ss.analog_read(pot)
    #we use a function to re-map the 0-1023 pot range to the 0-180 servo angle,
    #and we round the float off in the process
    potDegrees = round(translate(potValue, 0, 1023, 0, 180))
    crickit.servo_1.angle = potDegrees      # right
