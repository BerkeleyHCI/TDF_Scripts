import picamera     #camera library
import pygame as pg #audio library
import os           #communicate with os/command line

from google.cloud import vision  #gcp vision library
from time import sleep
from adafruit_crickit import crickit
import time
import signal
import sys
import re           #regular expression lib for string searches!
import subprocess


#set up your GCP credentials - replace the " " in the following line with your .json file and path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="TDF-VoiceVision.json"

# this line connects to Google Cloud Vision! 
client = vision.ImageAnnotatorClient()

# global variable for our image file - to be captured soon!
image = 'image.jpg'

def espeak(text: str, pitch: int=50) -> int:
    """ Use espeak to convert text to speech. """
    return subprocess.run(['espeak', f'-p {pitch}', text]).returncode

def takephoto(camera):
    
    # this triggers an on-screen preview, so you know what you're photographing!
    camera.start_preview() 
    sleep(.5)                   #give it a pause so you can adjust if needed
    camera.capture('image.jpg') #save the image
    camera.stop_preview()       #stop the preview

def ocr_handwriting(image):
    #this function sends your image to google cloud using the
    #text_detection method, collects a response, and parses that
    #response for all of the associated words detected.
    #these are captured as a single joined string in word_text.
    #if there is handwriting detected, strings are sent to motor_turn()
    #to determine if and how the motor should actuate!
    
    #these two lines connect to google cloud vision in the text_detection mode
    response = client.text_detection(image=image)
    text = response.full_text_annotation
    
    word_text = ""
    
    #this next block of code parses google cloud's response
    #down to words detected, which are combined into word_text
    for page in text.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    word_text += " "
                    word_text += ''.join([
                        symbol.text for symbol in word.symbols
                        ])                    

    #this next block checks if any word text was detected - and
    #if it was, the text and search strings are sent to motor_turn()

    if word_text:
        print('ocr_handwriting(): {}'.format(word_text))
        #espeak(word_text)
    else:
        print('ocr_handwriting(): No Handwriting Text Detected!')

def image_labeling(image):
    #this function sends your image to google cloud using the
    #label_detection method, collects a response, and parses that
    #response for all of the label descriptions collected - that is,
    #the AI's guesses at what is contained in the image.
    #each of these labels, identified as .description, are combined into
    #a single string label_text.
    #this time we'll be triggering different sounds - a bark or a meow! -
    #depending on what's in the image. 
    
    string1 = "dog"
    string2 = "cat"
    
    sound1 = "dog2.wav"
    sound2 = "cat.wav"
    
    response = client.label_detection(image=image)
    labels = response.label_annotations
       
    label_text = ""
    
    #this next block of code parses the various labels returned by google,
    #extracts the text descriptions, and combines them into a single string. 
    for label in labels:
        label_text += ''.join([label.description, " "])
    
    #if labels are identified, send the sound files, search strings, and label
    #text to speaker_out()
    if label_text:
        print('image_labeling(): {}'.format(label_text))
        speaker_out(sound1, sound2, label_text, string1, string2)
    else:
        print('image_labeling(): No Label Descriptions')   
       
def web_search(image):
    #this function sends your image to google cloud using the
    #web_detection method, collects a response, and parses that
    #response for the 'best web association' found for the image.
    #there's no actuation here - just printing - but you can easily
    #engage with speaker_out() or motor_turn() if you like!
    
    response = client.web_detection(image=image)
    web_guess = response.web_detection
    
    for label in web_guess.best_guess_labels:
        print('Best Web Guess Label: {}'.format(label.label))
    
def speaker_out(sound1, sound2, text, string1, string2):
    
    #this function plays sound1 
    #if string1 is found in the text descriptions returned
    #using regular expressions as in motor_turn().
    #similarly, sound 2 is played if string 2 is detected.
    #the pygame library is used to playback audio.
    #please note, if you're changing out sound files, 16-bit
    #.wav files are needed, otherwise you risk getting some
    #underrun errors. 
    
#    print(text)
    
    if re.search(string1, text, re.IGNORECASE):
        espeak("Dog")
   #     pg.mixer.music.load(sound1) #pygame - load the sound file
 #       pg.mixer.music.play()       #pygame - play the sound file
    elif re.search(string2, text, re.IGNORECASE):
        espeak("Cat")
 #       pg.mixer.music.load(sound2)
 #       pg.mixer.music.play()

def main():
    
    #generate a camera object for the takephoto function to
    #work with
    camera = picamera.PiCamera()
    
    #setup our pygame mixer to play audio in subsequent stages
  #  pg.init()
  #  pg.mixer.init()
    
    #this while loop lets the script run until you ctrl+c (command line)
    #or press 'stop' (Thonny IDE)
    while True:
 
        takephoto(camera) # First take a picture
        """Run a label request on a single image"""

        with open('image.jpg', 'rb') as image_file:
            #read the image file
            content = image_file.read()
            #convert the image file to a GCP Vision-friendly type
            image = vision.Image(content=content)
            #ocr_handwriting(image)
            image_labeling(image)
            #web_search(image)
            time.sleep(0.5)        
        
if __name__ == '__main__':
        main()    

