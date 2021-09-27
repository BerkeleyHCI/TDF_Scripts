import time
from adafruit_crickit import crickit
from adafruit_seesaw.neopixel import NeoPixel

from guizero import App, Text, TextBox, PushButton, Slider, Picture, Combo, CheckBox, ButtonGroup, info

ss = crickit.seesaw

num_pixels = 24  # Number of pixels driven from Crickit NeoPixel terminal

# The following line sets up a NeoPixel strip on Seesaw pin 20 for Feather
pixels = NeoPixel(crickit.seesaw, 20, num_pixels)
    
def change_color():
    pixels.fill((red_slider.value, green_slider.value, blue_slider.value))
    red_slider.bg = (red_slider.value, 0, 0)
    green_slider.bg = (0, green_slider.value, 0)
    blue_slider.bg = (0, 0, blue_slider.value)
    pixels.show() 

app = App(title="TDF GUI 3", width=800, height=500, layout="grid")

red_slider = Slider(app, command=change_color, width=600, height=80, grid=[2,1], start=0, end=255)
red_slider_description = Text(app, text="Red value:", grid=[1,1], align="left")

blue_slider = Slider(app, command=change_color, width=600, height=80, grid=[2,2], start=0, end=255)
blue_slider_description = Text(app, text="Blue value:", grid=[1,2], align="left")
blue_slider.sliderlength = 120
green_slider = Slider(app, command=change_color, width=600, height=80, grid=[2,3], start=0, end=255)
green_slider_description = Text(app, text="Green value:", grid=[1,3], align="left")

red_slider.bg = (0, 0, 0)
green_slider.bg = (0, 0, 0)
blue_slider.bg = (0, 0, 0)
app.display()