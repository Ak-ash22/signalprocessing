import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd

filepath = r'Users\14aka\OneDrive\Documents\Octave\Numerics\TDSound\PianoLaPeriod.wav'
data, samplerate = sf.read(filepath)
