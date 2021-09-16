# Drive NeoPixels on the NeoPixels Block on Crickit FeatherWing
import time
from adafruit_crickit import crickit
from adafruit_seesaw.neopixel import NeoPixel

ss = crickit.seesaw

num_pixels = 24  # Number of pixels driven from Crickit NeoPixel terminal

# The following line sets up a NeoPixel strip on Seesaw pin 20 for Feather
pixels = NeoPixel(crickit.seesaw, 20, num_pixels)
        
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
BLANK = (0, 0, 0)
customAdam = (120, 210, 12)

while True:

    print("blank")
    pixels.fill(BLANK)
    pixels.show()
    time.sleep(1)

    print("red")
    pixels.fill(RED)
    pixels.show()
    time.sleep(1)

    print("yellow")
    pixels.fill(YELLOW)
    pixels.show()
    time.sleep(1)

    print("a color Adam came up with")
    pixels.fill(customAdam)
    pixels.show()
    time.sleep(1)

    print("some other color that doesn't have an assigned name")
    pixels.fill((18, 25, 125))
    pixels.show()
    time.sleep(1)
