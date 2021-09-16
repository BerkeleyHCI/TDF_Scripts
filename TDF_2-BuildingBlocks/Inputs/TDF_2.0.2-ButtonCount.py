import time
from adafruit_crickit import crickit
ss = crickit.seesaw
BUTTON_1 = crickit.SIGNAL1 
ss.pin_mode(BUTTON_1, ss.INPUT_PULLUP)
buttonOnePrev = False  # stores value of last iteration
buttonOneCurr = False  # stores value of current iteration
buttonPresses = 0 #stores number of presses since script start

while True:
  time.sleep(.1)
  buttonOnePrev = buttonOneCurr
  buttonOneCurr = ss.digital_read(BUTTON_1)
  if buttonOneCurr and not buttonOnePrev:
    print("button falling edge")
  elif not buttonOneCurr and buttonOnePrev: 
    print("button rising edge")
    buttonPresses=buttonPresses+1
    print(buttonPresses)
  elif buttonOneCurr and buttonOnePrev:
    print("button is not pressed")
  else:
    print("button is  pressed")
