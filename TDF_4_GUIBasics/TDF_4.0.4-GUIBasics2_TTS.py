# This material (or a version thereof) can be found at
# http:\\www.projects.raspberrypi.org/en/projects/getting-started-with-guis
# Modified by Adam Hutz for TDF, 2021

# See http:\\www.lawsie.github.io/guizero/widgetoverview for documentation
import time
import subprocess

color_1 = "#3C3744"
color_2 = "#EF476F"
color_3 = "#1B9AAA"
color_4 = "#C4C6E7"
color_5 = "#F6F4D2"

language = "en" #try en, en-us, en-sc, en-rp, en-n, en-rp, en-wm, zh (mandarin), el (greek), es (spanish)
genderIdentity = "+f3" #m1 - m7, f1 - f5
# add +croak or +whisper for other effects
# find other variants with command line: espeak --voices=variant
# also check out espeak.sourceforge.net/

from guizero import App, Text, TextBox, PushButton, Slider, Picture, Combo, CheckBox, ButtonGroup, info

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
                subprocess.Popen(["espeak", "-v", language+genderIdentity, "Banana-Banana"])
            else:
                time.sleep(processing_time)
                subprocess.Popen(["espeak", "-v", language+genderIdentity, "Bananana"])

        elif (fruit_two.value == "Avocado"):
            if (blended_thoroughly.value == 0):
                time.sleep(processing_time)
                subprocess.Popen(["espeak", "-v", language+genderIdentity, "Banana-Avocado"])
            else:
                time.sleep(processing_time)
                subprocess.Popen(["espeak", "-v", language+genderIdentity, "Banavocado"])
        elif (fruit_two.value == "Apple"):
            if (blended_thoroughly.value == 0):
                time.sleep(processing_time)
                subprocess.Popen(["espeak", "-v", language+genderIdentity, "Banana-Apple"])
            else:
                time.sleep(processing_time)
                subprocess.Popen(["espeak", "-v", language+genderIdentity, "Banapple"])
                
    if (fruit_one.value == "Avocado"):
        if (fruit_two.value == "Banana"):
            if (blended_thoroughly.value == 0):
                time.sleep(processing_time)
                subprocess.Popen(["espeak", "-v", language+genderIdentity, "Avocado-Banana"])
            else:
                time.sleep(processing_time)
                subprocess.Popen(["espeak", "-v", language+genderIdentity, "Avocadana"])
        elif (fruit_two.value == "Avocado"):
            if (blended_thoroughly.value == 0):
                time.sleep(processing_time)
                subprocess.Popen(["espeak", "-v", language+genderIdentity, "Avocado-Avocado"])
            else:
                time.sleep(processing_time)
                subprocess.Popen(["espeak", "-v", language+genderIdentity, "Avocadavo"])
        elif (fruit_two.value == "Apple"):
            if (blended_thoroughly.value == 0):
                time.sleep(processing_time)
                subprocess.Popen(["espeak", "-v", language+genderIdentity, "Avocado-Apple"])
            else:
                time.sleep(processing_time)
                subprocess.Popen(["espeak", "-v", language+genderIdentity, "Avocadapple"])
                

    if (fruit_one.value == "Apple"):
        if (fruit_two.value == "Banana"):
            if (blended_thoroughly.value == 0):
                time.sleep(processing_time)
                subprocess.Popen(["espeak", "-v", language+genderIdentity, "Apple-Banana"])
            else:
                time.sleep(processing_time)
                subprocess.Popen(["espeak", "-v", language+genderIdentity, "Applana"])
        elif (fruit_two.value == "Avocado"):
            if (blended_thoroughly.value == 0):
                time.sleep(processing_time)
                subprocess.Popen(["espeak", "-v", language+genderIdentity, "Apple-Avocado"])
            else:
                time.sleep(processing_time)
                subprocess.Popen(["espeak", "-v", language+genderIdentity, "Applavocado"])
        elif (fruit_two.value == "Apple"):
            if (blended_thoroughly.value == 0):
                time.sleep(processing_time)
                subprocess.Popen(["espeak", "-v", language+genderIdentity, "Apple-Apple"])
            else:
                time.sleep(processing_time)
                subprocess.Popen(["espeak", "-v", language+genderIdentity, "Applapple"])
                
          
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
