from guizero import App, PushButton
import time
from adafruit_crickit import crickit

#for vibration motor on motor driver 1
crickit.drive_1.frequency = 1000

#for servo on servo position 1
ss = crickit.seesaw
crickit.servo_1.set_pulse_width_range(min_pulse=500, max_pulse=2500)


def start():
    start_button.disable()
    #crickit.drive_1.fraction = 1.0
    #crickit.servo_1.angle = 180
    stop_button.enable()

def stop():
    start_button.enable()
    #crickit.drive_1.fraction = 0
    #crickit.servo_1.angle = 0
    stop_button.disable()

app = App(title="TDF GUI, ON/OFF", width=800, height=500)
start_button = PushButton(app, command=start, text="start", width="fill", height="fill")
stop_button = PushButton(app, command=stop, text="stop", width="fill", height="fill", enabled=False)
app.display()
