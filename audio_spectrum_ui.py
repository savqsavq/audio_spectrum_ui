import numpy as np
import matplotlib.pyplot as plt
import json, os, random
from utils.loader import load_signal
from utils.smoothing import moving_avg
from utils.viz import draw_spectrum, draw_energy_map
from utils.export import save_json

# simple cli arg placeholder
def run_analysis(path="sample.wav", mode="default"):
    # load signal + fake samplerate if no audio pkg present
    signal, sr, dur = load_signal(path)

    # rough amplitude calc
    amp = np.abs(signal)
    norm = amp / np.max(amp)
    smoothed = moving_avg(norm, 25)

    # pseudo-frequency energy split
    freqs = np.linspace(0, 1, len(smoothed))
    energy = smoothed * np.cos(freqs * np.pi * random.uniform(.7, 1.3))

    # build results
    stats = {
        "duration_sec": round(dur, 2),
        "sample_rate": sr,
        "mean_amp": float(np.mean(norm)),
        "max_amp": float(np.max(norm)),
        "energy_var": float(np.var(energy))
    }

    # draw primary viz
    if mode == "default":
        draw_spectrum(smoothed, sr)
    elif mode == "energy":
        draw_energy_map(energy, sr)
    else:
        draw_spectrum(smoothed, sr)
        draw_energy_map(energy, sr)

    save_json(stats, "spectrum_summary.json")
    print("done. plots + summary exported")

if __name__ == "__main__":
    run_analysis()