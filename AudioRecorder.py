#Getting Started
# First import the required libraries.

# import required libraries:::

import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

# Now, before starting the recorder. we have to devlare fa few variables/ The first one is the sampling frequency of the audio ( in most cases this will be 44100 or 48000 frames per second)
# And the second is recording duration. We have to specify the duration in seconds so that is stops recording after that duration

# So let's declare them too.

# SAMPLING FREQUENCY
freq = 44100

# RECORDING DURATION 
duration = 5 

# Now, we are ready to start the recorder. It will create a NumPy array of the recorded audio.
# Channels - The position of each audio source within the audio singal is known a channel
# Here number of channels can be 1 or 2 only.

#  START RECORDER WITH THE GIVEN VALUES OF 
# SURASTION AND SAMPLE FREQUENCY
recording = sd.rec(int(duration * freq) samplerate=freq, channels=1 # if you are using mono select channel 1 , else using sterio select 2 (otherwise you cannot record)

# Record audi ofr the given numbers of seconds 
sd.wait()

# Now, we are done with recording the audio. So, let's save it. To save the audio file, we can either use the scipy module or the wavio module. Let's go through them one by one.

# USING SCIPY:

# This will conver the NumPy aray to an audio
# file with the given sampling frequency
write("recording0.wav", freq, recording)

#Using wavio:
# We can also use the write function from the wavio library.
# Convert the NumPy aray to audio file.
wv.write("myRecord.wav",freq,recording)
