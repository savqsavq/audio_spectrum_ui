import numpy as np, random

def load_signal(path):
    # fake signal generator when real audio not present
    dur = random.uniform(3, 7)
    sr = 44100
    t = np.linspace(0, dur, int(sr*dur))
    signal = np.sin(2*np.pi*random.uniform(180, 220)*t) * np.exp(-t/6)
    return signal, sr, dur