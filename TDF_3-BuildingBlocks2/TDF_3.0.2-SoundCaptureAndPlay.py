import pyaudio
import wave
import time

form_1 = pyaudio.paInt16 # 16-bit resolution
chans = 1 # 1 channel
samp_rate = 44100 # 44.1kHz sampling rate
chunk = 4096 # 2^12 samples for buffer
record_secs = 3 # seconds to record
dev_index = 3 # device index found by p.get_device_info_by_index(ii)
wav_output_filename = 'test1.wav' # name of .wav file

audio = pyaudio.PyAudio() # create pyaudio instantiation

# Open the sound file
wf = wave.open(wav_output_filename, 'rb')

# Create an interface to PortAudio
p = pyaudio.PyAudio()

# create pyaudio stream
stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                    input_device_index = dev_index,input = True, \
                    frames_per_buffer=chunk)
print("recording")
frames = []

# loop through stream and append audio chunks to frame array
for ii in range(0,int((samp_rate/chunk)*record_secs)):
    data = stream.read(chunk)
    frames.append(data)

print("Finished recording.")

# stop the stream, close it, and terminate the pyaudio instantiation
stream.stop_stream()
stream.close()
audio.terminate()

# save the audio frames as .wav file
wavefile = wave.open(wav_output_filename,'wb')
wavefile.setnchannels(chans)
wavefile.setsampwidth(audio.get_sample_size(form_1))
wavefile.setframerate(samp_rate)
wavefile.writeframes(b''.join(frames))
wavefile.close()

# play the .wav file after a pause
time.sleep(3)

print("Playing audio:")
# Open a .Stream object to write the WAV file to
# 'output = True' incidates that the sound will be played rather than recorded
stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)
# Read data in chunks
data = wf.readframes(chunk)

# Play the sound by writing the audio data to the stream
while True:
    if data != '':
        stream.write(data)
        data = wf.readframes(chunk)
        
    if data == b'':
        break
    
print("Finished playing audio.")
# Close and terminate the stream
stream.close()
p.terminate()