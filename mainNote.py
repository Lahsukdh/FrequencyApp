import numpy as np
import aubio
import pyaudio

RATE = 44100
CHUNK = 2048
FORMAT = pyaudio.paInt16
CHANNELS = 1

p = pyaudio.PyAudio()
print("Starting stream")
stream = p.open(format=FORMAT, channels=CHANNELS, input=True, frames_per_buffer=CHUNK, rate=44100)

try :
    while(True) : 
        data = stream.read(CHUNK)
        samples = np.frombuffer(data, dtype=np.int16)
        fft_result = np.fft.rfft(samples)

        amp = np.abs(fft_result)

        peak = np.argmax(amp)

        print(peak)
except KeyboardInterrupt:
    print("Ending stream...")
    stream.stop_stream()