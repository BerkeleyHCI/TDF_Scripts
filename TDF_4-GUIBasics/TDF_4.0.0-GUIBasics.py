# This material (or a version thereof) can be found at
# http:\\www.projects.raspberrypi.org/en/projects/getting-started-with-guis
# Modified by Adam Hutz for TDF, 2021

from guizero import App, Text, PushButton, Slider, Picture
      
def yes_good():
    my_jack.show()
    create_image.disable()
    destroy_image.enable()
    
def next_this():
    my_jack.hide()
    create_image.enable()
    destroy_image.disable()
    
def change_text_size(slider_value):
    header_message.size = slider_value

app = App(title="TDF GUI 1")

#header_message = Text(app, text="Check out my first Raspberry Pi GUI!", size=20, font="Lato", color="#6b09e0")
#text_size = Slider(app, command=change_text_size, width=400, height=40, start=10, end=50)
#create_image = PushButton(app, command=yes_good, text="Push this button", width=40)
#destroy_image = PushButton(app, command=next_this, text="Then push this button", width=40)
#my_jack = Picture(app, image="jack.gif")

#next_this()
app.display()