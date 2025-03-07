'''NOt Useful as it counts the sound '''
import pyaudio
import numpy as np
import time

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Define microphone settings
FORMAT = pyaudio.paInt16  # 16-bit audio format
CHANNELS = 2  # Mono audio
RATE = 44100  # Samples per second
CHUNK = 1024  # Number of frames per buffer
THRESHOLD = 10000  # Sensitivity to detect claps
CLAP_DELAY = 0.-1  # Minimum time between claps

# Open the microphone stream
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, 
                    input=True, frames_per_buffer=CHUNK)

clap_count = 0
last_clap_time = time.time()

print("\n🎤 Listening for claps... (Press Ctrl+C to stop)\n")

try:
    while True:
        # Read audio input
        data = np.frombuffer(stream.read(CHUNK, exception_on_overflow=False), dtype=np.int16)
        amplitude = np.max(np.abs(data))  # Get the highest sound peak

        # Detect a clap (sound peak crosses the threshold)
        if amplitude > THRESHOLD:
            current_time = time.time()
            
            # Avoid multiple detections for the same clap
            if current_time - last_clap_time > CLAP_DELAY:
                clap_count += 1
                print(f"👏 Clap detected! Total claps: {clap_count}")
                last_clap_time = current_time  # Update the last clap time

except KeyboardInterrupt:
    print("\n🛑 Stopping Clap Counter...")

# Close the audio stream
stream.stop_stream()
stream.close()
audio.terminate()
