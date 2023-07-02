import numpy as np
import sounddevice as sd

samplerate = 44100  # Sample rate
duration = 5  # Duration of the sound in seconds
frequency = 440  # Frequency of the sound in Hz

# Generate the initial waveform using a impulse response
impulse = np.zeros(int(samplerate / frequency))
impulse[0] = 1
impulse = np.cumsum(impulse)
impulse *= 2 * frequency / samplerate

# Apply the Karplus-Strong algorithm to generate the sound
samples = np.zeros(int(samplerate * duration))
N = int(samplerate / frequency)
for i in range(N, int(len(samples) - N)):
    samples[i] = 0.5 * (samples[i - N] + samples[i + N]) + 2 * np.random.rand() - 1

samples *= np.tile(impulse, int(len(samples) / len(impulse)))

sd.play(samples, samplerate)

status = sd.wait()  # Wait until the sound has finished playing
