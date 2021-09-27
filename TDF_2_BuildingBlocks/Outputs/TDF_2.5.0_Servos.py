import time
from adafruit_crickit import crickit
 
ss = crickit.seesaw

crickit.servo_1.set_pulse_width_range(min_pulse=500, max_pulse=2500)

while True:

    crickit.servo_1.angle = 0
    time.sleep(2)
    crickit.servo_1.angle = 180
    time.sleep(2)
