import numpy as np
import aubio
import pyaudio

RATE = 48000
CHUNK = 8192
FORMAT = pyaudio.paInt16
CHANNELS = 1




p = pyaudio.PyAudio()
print("Starting stream")
stream = p.open(format=FORMAT, channels=CHANNELS, input=True, frames_per_buffer=CHUNK, rate=RATE)

try :
    while(True) : 
        data = stream.read(CHUNK)
        samples = np.frombuffer(data, dtype=np.int16)
        fft_result = np.fft.rfft(samples)   

        amp = np.abs(fft_result)

        peak = np.argmax(amp)

        volume = np.mean(np.abs(samples))
        freqs = np.fft.rfftfreq(CHUNK, d=1/RATE)
        peak_freq = freqs[peak]

        if volume > 1000 :
            print(aubio.freq2note(peak_freq))


except KeyboardInterrupt:
    print("Ending stream...")
    stream.stop_stream()
    stream.close()
    p.terminate()
    