# Vivek Rao, Technology Design Foundations @ UC-Berkeley 2021
# This script is heavily based on some excellent material from Dr. Adrian Rosebrock,
# Specifically: Adrian Rosebrock, Face Alignment with OpenCV and Python,
# (retrieved June 25, 2017), http://www.pyimagesearch.com/2017/05/22/face-alignment-with-opencv-and-python/
# This script uses Haar Cascades for compute-light face detection
# And Dr. Rosebrock's imutils package for working with streaming video on-device.
# Here, we'll take a live video feed from your pi Camera, and change the color
# of the neopixel depending on which side of the frame a face is in -
# red for right, green for left. 

# import the necessary packages
from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2
import time
from adafruit_crickit import crickit
from adafruit_seesaw.neopixel import NeoPixel

ss = crickit.seesaw

num_pixels = 24  # Number of pixels driven from Crickit NeoPixel terminal

# The following line sets up a NeoPixel strip on Seesaw pin 20 for Feather
pixels = NeoPixel(crickit.seesaw, 20, num_pixels)        
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
BLANK = (0, 0, 0)

# load the haar cascade face detector from
print("loading face detector .xml...")
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# initialize the video stream and allow the camera sensor to warm up
print("Video Warm-Up")
vs = VideoStream(src=0).start()
pixels.fill(BLANK)
time.sleep(2.0)

# loop over the frames from the video stream
while True:
# grab the frame from the video stream, resize it, and convert it
# to grayscale
    frame = vs.read()
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # perform face detection
    # rects returns  bounding box coordinates for faces detected
    # the format is a tuple of lists; more than one face detected
    # will result in multiple boxes returned
    rects = detector.detectMultiScale(gray, scaleFactor=1.05,
        minNeighbors=5, minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE)
    
    #uncomment the below line to see the kind of data returned
    #from the face detection work! 
    #print(rects, len(rects))
    
    # loop over the bounding boxes
    for (x, y, w, h) in rects:
        # draw the face bounding box on the image
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        if x < 150:
            pixels.fill(RED)
        elif x < 300:
            pixels.fill(GREEN)
        else:
            pixels.fill(BLANK)
        
    # show the output frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

# close the video frame
cv2.destroyAllWindows()
vs.stop()
