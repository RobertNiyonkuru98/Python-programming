import pyaudio
import numpy as np

p = pyaudio.PyAudio()
# Let's open the stream
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100,
                input=True, frames_per_buffer=1024)

print("--- MIC TEST STARTING ---")
print("Speak or clap to see the volume levels...")

try:
    for i in range(1000): # Run for about 5 seconds
        data = np.frombuffer(stream.read(1024, exception_on_overflow=False), dtype=np.int16)
        peak = np.average(np.abs(data))
        # This will show you exactly what the computer 'hears'
        print(f"Current Volume Level: {int(peak)}")
except Exception as e:
    print(f"Error: {e}")
finally:
    stream.stop_stream()
    stream.close()
    p.terminate()