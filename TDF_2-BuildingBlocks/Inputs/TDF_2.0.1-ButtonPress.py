# libraries go here
import time
from adafruit_crickit import crickit

# variables go here
ss = crickit.seesaw
BUTTON_1 = crickit.SIGNAL1 
buttonOnePrev = False  # stores value of last iteration
buttonOneCurr = False  # stores value of current iteration
buttonPresses = 0 #stores number of presses since script start

# pin mode functions go here
ss.pin_mode(BUTTON_1, ss.INPUT_PULLUP)

# main function goes here

while True:
  time.sleep(.1)				# wait a millisecond per loop to slow down interaction
  buttonOnePrev = buttonOneCurr			# reset our "reading" of the button
  buttonOneCurr = ss.digital_read(BUTTON_1)	# actually read the button and set that to a variable called "buttonOneCurr"
  if buttonOneCurr and not buttonOnePrev:	# if new reading is false and old reading was true, button was just un-pressed
    print("button falling edge")		# print this information to the shell (for debubugging)
  elif not buttonOneCurr and buttonOnePrev: 	# if new reading is true and old reading was false, button was just pressed
    print("button rising edge")			# print this information to the shell
    buttonPresses=buttonPresses+1		# add one number to the number of button presses counter
    print(buttonPresses)			# print that info
						# this is where you can put things that happen continuously while button is pressed



  elif buttonOneCurr and buttonOnePrev:		# if new reading and old reading both false...
    print("button is not pressed")		# print that info
  else:						# only other circumstance: both readings "true"
    print("button is  pressed")			# print that info
						# this is where you can put things that happen continuously while button is pressed
 

