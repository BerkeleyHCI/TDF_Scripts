# This material (or a version thereof) can be found at
# http:\\www.projects.raspberrypi.org/en/projects/getting-started-with-guis
# Modified by Adam Hutz for TDF, 2021

# See http:\\www.lawsie.github.io/guizero/widgetoverview for documentation
import time
from guizero import App, Text, TextBox, PushButton, Slider, Picture, Combo, CheckBox, ButtonGroup, info

color_1 = "#3C3744"
color_2 = "#EF476F"
color_3 = "#1B9AAA"
color_4 = "#C4C6E7"
color_5 = "#F6F4D2"

def do_blending():
    info("Blending", "Fruits blending...")
    print( fruit_one.value)
    print( blended_thoroughly.value)
    print( for_when.value)
    processing_time = int(for_when.value)
    
    if (fruit_one.value == "Banana"):
        if (fruit_two.value == "Banana"):
            if (blended_thoroughly.value == 0):
                time.sleep(processing_time)
                info("Results:", "Banana-Banana")
            else:
                time.sleep(processing_time)
                info("Results:", "Bananana")
        elif (fruit_two.value == "Avocado"):
            if (blended_thoroughly.value == 0):
                time.sleep(processing_time)
                info("Results:", "Banana-Avocado")
            else:
                time.sleep(processing_time)
                info("Results:", "Banavocando")
        elif (fruit_two.value == "Apple"):
            if (blended_thoroughly.value == 0):
                time.sleep(processing_time)
                info("Results:", "Banana-Apple")
            else:
                time.sleep(processing_time)
                info("Results:", "Banapple")
                
    if (fruit_one.value == "Avocado"):
        if (fruit_two.value == "Banana"):
            if (blended_thoroughly.value == 0):
                time.sleep(processing_time)
                info("Results:", "Avocado-Banana")
            else:
                time.sleep(processing_time)
                info("Results:", "Avocadana")
        elif (fruit_two.value == "Avocado"):
            if (blended_thoroughly.value == 0):
                time.sleep(processing_time)
                info("Results:", "Avocado-Avocado")
            else:
                time.sleep(processing_time)
                info("Results:", "Avocadavo")
        elif (fruit_two.value == "Apple"):
            if (blended_thoroughly.value == 0):
                time.sleep(processing_time)
                info("Results:", "Avocado-Apple")
            else:
                time.sleep(processing_time)
                info("Results:", "Avocadapple")
                

    if (fruit_one.value == "Apple"):
        if (fruit_two.value == "Banana"):
            if (blended_thoroughly.value == 0):
                time.sleep(processing_time)
                info("Results:", "Apple-Banana")
            else:
                time.sleep(processing_time)
                info("Results:", "Aplana")
        elif (fruit_two.value == "Avocado"):
            if (blended_thoroughly.value == 0):
                time.sleep(processing_time)
                info("Results:", "Apple-Avocado")
            else:
                time.sleep(processing_time)
                info("Results:", "Aplavocado")
        elif (fruit_two.value == "Apple"):
            if (blended_thoroughly.value == 0):
                time.sleep(processing_time)
                info("Results:", "Apple-Apple")
            else:
                time.sleep(processing_time)
                info("Results:", "Aplaple")
                
            
app = App(title="TDF GUI 2", bg=color_1, width=800, height=500, layout="grid")

fruit_one_description = Text(app, text="First fruit:", color=color_5, size=40, grid=[1,1], align="left")
fruit_one = Combo(app, options=["Banana", "Apple", "Avocado"], width=40, height=3, grid=[2,1], align="left")
fruit_one.bg = color_4

fruit_two_description = Text(app, text="Second fruit:", color=color_5, size=40, grid=[1,2], align="left")
fruit_two = Combo(app, options=["Banana", "Apple", "Avocado"], width=40, height=3, grid=[2,2], align="left")
fruit_two.bg = color_4

for_when_description = Text(app, text="For when?", color=color_5, size=40, grid=[1,3], align="left")
for_when = ButtonGroup(app, options=[["Now", "0"], ["5 seconds", "5"], ["10 seconds", "10"]], height=12, width=11, horizontal=True, grid=[2,3], align="left")
for_when.bg = color_4

blend_thoroughly_description = Text(app, text="Blend thoroughly?", color=color_5, size=40, grid=[1,4], align="left")
blended_thoroughly = CheckBox(app, text="Yes", grid=[2,4], align="left", width=44, height=3)
blended_thoroughly.bg=color_3

space = Text(app, text="", color=color_3, size=40, grid=[1,5], align="left")

order = PushButton(app, command=do_blending, text="Blend fruits!", width=40, height="2", grid=[1,6,2,2], align="bottom")
order.text_color=color_1
order.text_size=20
order.bg=color_2

app.display()
