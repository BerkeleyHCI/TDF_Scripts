# Drive NeoPixels on the NeoPixels Block on Crickit FeatherWing
import time
from adafruit_crickit import crickit
from adafruit_seesaw.neopixel import NeoPixel

pot = crickit.SIGNAL2
ss = crickit.seesaw

num_pixels = 24  # Number of pixels driven from Crickit NeoPixel terminal
 
ss.pin_mode(pot, ss.INPUT)

# The following line sets up a NeoPixel strip on Seesaw pin 20 for Feather
pixels = NeoPixel(crickit.seesaw, 20, num_pixels)
 
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)
    
def pot_chase(wait):

    for j in range(255):
        potValue = ss.analog_read(pot)
        potColorValue = round(translate(potValue, 0, 1023, 0, 255))
        print((potColorValue))
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + potColorValue
            pixels[i] = wheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)
        
def translate(value, leftMin, leftMax, rightMin, rightMax): #Adam Luchjenbroers, 12/8/2009
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)
        
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
BLANK = (0, 0, 0)
 
while True:

    print("blank")
    pixels.fill(BLANK)
    pixels.show()
    time.sleep(3)
    
    pot_chase(0)
