import time
from adafruit_crickit import crickit
 
print("1 Drive demo!")
 
crickit.drive_1.frequency = 1000
 
while True:
    crickit.drive_1.fraction = 1.0  # all the way on
    time.sleep(0.5)
    crickit.drive_1.fraction = 0.0  # all the way off
    time.sleep(0.5)
    crickit.drive_1.fraction = 0.5  # half on/off
    time.sleep(0.5)
    # and repeat!