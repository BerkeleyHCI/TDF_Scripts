import time
from adafruit_crickit import crickit
 
print("1 Servo demo!")
 
#uncomment for custom pulse widths
#crickit.servo_1.set_pulse_width_range(min_pulse=500, max_pulse=2500)

while True:
    print("Moving servo #1")
    crickit.servo_1.angle = 0      # right
    time.sleep(1)
    crickit.servo_1.angle = 90     # middle
    time.sleep(1)
    crickit.servo_1.angle = 180    # left
    time.sleep(1)
    crickit.servo_1.angle = 90     # middle
    time.sleep(1)
    # and repeat!
