from __future__ import division

import re
import sys
import os

from google.cloud import speech_v1
import pyaudio #for recording audio!
import pygame  #for playing audio
from six.moves import queue

from gtts import gTTS
import os
import time
from adafruit_crickit import crickit
from adafruit_seesaw.neopixel import NeoPixel
 
num_pixels = 24  # Number of pixels driven from Crickit NeoPixel terminal
 
# The following line sets up a NeoPixel strip on Seesaw pin 20 for Feather
pixels = NeoPixel(crickit.seesaw, 20, num_pixels)

# Audio recording parameters, set for our USB mic.
RATE = 44100 #if you change mics - be sure to change this :)
CHUNK = int(RATE / 10)  # 100ms

credential_path = "/home/pi/TDF-GCPSpeech/TDF-VoiceVision.json" #or replace with your file name!
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=credential_path

pygame.init()
pygame.mixer.init()
#MicrophoneStream() is brought in from Google Cloud Platform
class MicrophoneStream(object):
    """Opens a recording stream as a generator yielding the audio chunks."""
    def __init__(self, rate, chunk):
        self._rate = rate
        self._chunk = chunk

        # Create a thread-safe buffer of audio data
        self._buff = queue.Queue()
        self.closed = True

    def __enter__(self):
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            # The API currently only supports 1-channel (mono) audio
            # https://goo.gl/z757pE
            channels=1, rate=self._rate,
            input=True, frames_per_buffer=self._chunk,
            # Run the audio stream asynchronously to fill the buffer object.
            # This is necessary so that the input device's buffer doesn't
            # overflow while the calling thread makes network requests, etc.
            stream_callback=self._fill_buffer,
        )

        self.closed = False

        return self

    def __exit__(self, type, value, traceback):
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        # Signal the generator to terminate so that the client's
        # streaming_recognize method will not block the process termination.
        self._buff.put(None)
        self._audio_interface.terminate()

    def _fill_buffer(self, in_data, frame_count, time_info, status_flags):
        """Continuously collect data from the audio stream, into the buffer."""
        self._buff.put(in_data)
        return None, pyaudio.paContinue

    def generator(self):
        while not self.closed:
            # Use a blocking get() to ensure there's at least one chunk of
            # data, and stop iteration if the chunk is None, indicating the
            # end of the audio stream.
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]

            # Now consume whatever other data's still buffered.
            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                except queue.Empty:
                    break

            yield b''.join(data)

#this loop is where the microphone stream gets sent
def listen_print_loop(responses):
    """Iterates through server responses and prints them.

    The responses passed is a generator that will block until a response
    is provided by the server.

    Each response may contain multiple results, and each result may contain
    multiple alternatives; for details, see https://goo.gl/tjCPAU.  Here we
    print only the transcription for the top alternative of the top result.

    In this case, responses are provided for interim results as well. If the
    response is an interim one, print a line feed at the end of it, to allow
    the next result to overwrite it, until the response is a final one. For the
    final one, print a newline to preserve the finalized transcription.
    """
    num_chars_printed = 0
    for response in responses:
        if not response.results:
            continue

        # The `results` list is consecutive. For streaming, we only care about
        # the first result being considered, since once it's `is_final`, it
        # moves on to considering the next utterance.
        result = response.results[0]
        if not result.alternatives:
            continue

        # Display the transcription of the top alternative.
        transcript = result.alternatives[0].transcript

        # Display interim results, but with a carriage return at the end of the
        # line, so subsequent lines will overwrite them.
        #
        # If the previous result was longer than this one, we need to print
        # some extra spaces to overwrite the previous result
        overwrite_chars = ' ' * (num_chars_printed - len(transcript))

        if not result.is_final:
            #sys.stdout.write(transcript + overwrite_chars + '\r')
            #sys.stdout.flush()

            num_chars_printed = len(transcript)

        else:
            print(transcript + overwrite_chars)
            #if there's a voice activitated quit - quit!
            if re.search(r'\b(exit|quit)\b', transcript, re.I):
                print('Exiting..')
                break
            else:
                decide_action(transcript)
#            print(transcript)
            # Exit recognition if any of the transcribed phrases could be
            # one of our keywords.
            num_chars_printed = 0

def decide_action(transcript):
    
    #here we're using some simple code on the final transcript from
    #GCP to figure out what to do, how to respond. 
    
    if re.search('on',transcript, re.I):
        LED_Action(1)
    elif re.search('off',transcript, re.I):
        LED_Action(2)
    elif re.search('blink',transcript, re.I):
        LED_Action(3)
    elif re.search('bears',transcript, re.I):
        Motor_Action('bears')
    elif re.search('cardinal',transcript, re.I):
        Motor_Action('cardinal')
    elif re.search('fairest',transcript, re.I):
        Fairest()
    elif re.search('repeat',transcript, re.I):
        repeat(transcript)
    else:
        idontknow()
        

def LED_Action(numbers):
    ss = crickit.seesaw

    RED = (255, 0, 0)
    YELLOW = (255, 150, 0)
    GREEN = (0, 255, 0)
    CYAN = (0, 255, 255)
    BLUE = (0, 0, 255)
    PURPLE = (180, 0, 255)
    OFF = (0,0,0)
 
    print("initialize off")
    pixels.fill(OFF)
    
    if numbers == 3:
        pixels.fill(RED)
        time.sleep(0.5)
        pixels.fill(OFF)
        time.sleep(0.5)
        pixels.fill(RED)
        pixels.fill(RED)
        time.sleep(0.5)
        pixels.fill(OFF)
        time.sleep(0.5)
        pixels.fill(RED)
        
    elif numbers == 2:
        pixels.fill(OFF)
        time.sleep(0.5)
    elif numbers == 1:
        pixels.fill(PURPLE)
        time.sleep(0.5)
     

def Motor_Action(bears):
    
    if bears == 'bears':
        pygame.mixer.init()
        pygame.mixer.music.load('gobears.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy(): 
            pygame.time.Clock().tick(10)
        crickit.servo_1.angle = 0      # right
        time.sleep(1)
    elif bears == 'cardinal':
        pygame.mixer.init()
        pygame.mixer.music.load('boo.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy(): 
            pygame.time.Clock().tick(10)
        crickit.servo_1.angle = 180
        time.sleep(1)
        
def Fairest():
    pygame.mixer.init()
    pygame.mixer.music.load('fairest.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy(): 
        pygame.time.Clock().tick(10)

def repeat(transcript):
    t2s = gTTS('You said {}'.format(transcript), lang ='en')
    t2s.save('repeat.mp3')
    
    pygame.mixer.init()
    pygame.mixer.music.load('repeat.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy(): 
        pygame.time.Clock().tick(10)

def idontknow():
    pygame.mixer.init()
    pygame.mixer.music.load('idontknow.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy(): 
        pygame.time.Clock().tick(10)

def main():
    
    #setting up the GTTS responses as .mp3 files!
    t2s = gTTS('You are the fairest of them all!', lang ='en')
    t2s.save('fairest.mp3')
    t2s = gTTS('You didnt tell me what to do with that.', lang='en')
    t2s.save('idontknow.mp3')
    t2s = gTTS('Go bears!', lang='en')
    t2s.save('gobears.mp3')
    t2s = gTTS('Boo oo oo oo oo!')
    t2s.save('boo.mp3')
    
    # See http://g.co/cloud/speech/docs/languages
    # for a list of supported languages.
    # this code comes from Google Cloud's Speech to Text API!
    # Check out the links in your handout. Comments are ours.
    language_code = 'en-US'  # a BCP-47 language tag

    #set up a client
    client = speech_v1.SpeechClient()
    #make sure GCP is aware of the encoding, rate 
    config = speech_v1.RecognitionConfig(
        encoding=speech_v1.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code=language_code)
    #our example uses streamingrecognition - most likely what you will want to use.
    #check out the simpler cases of asychronous recognition too!
    streaming_config = speech_v1.StreamingRecognitionConfig(
        config=config,
        interim_results=True)
    
    #this section is where the action happens:
    #a microphone stream is set up, requests are generated based on
    #how the audiofile is chunked, and they are sent to GCP using
    #the streaming_recognize() function for analysis. responses
    #contains the info you get back from the API. 
    with MicrophoneStream(RATE, CHUNK) as stream:
        audio_generator = stream.generator()
        requests = (speech_v1.StreamingRecognizeRequest(audio_content=content)
                    for content in audio_generator)

        responses = client.streaming_recognize(streaming_config, requests)

        # Now, put the transcription responses to use.
        listen_print_loop(responses)


if __name__ == '__main__':
    main()
