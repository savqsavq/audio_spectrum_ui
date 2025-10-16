import matplotlib.pyplot as plt
import numpy as np, random

def draw_spectrum(data, sr):
    x = np.linspace(0, len(data)/sr, len(data))
    plt.plot(x, data, color="#b36fca", lw=1)
    plt.title("spectrum amplitude decay")
    plt.xlabel("time (s)")
    plt.ylabel("normalized amp")
    plt.savefig("spectrum_plot.png", dpi=120)
    plt.close()

def draw_energy_map(energy, sr):
    plt.imshow(np.expand_dims(energy, axis=0),
               aspect="auto", cmap="plasma",
               extent=[0, len(energy)/sr, 0, 1])
    plt.title("energy intensity map")
    plt.xlabel("time (s)")
    plt.savefig("energy_map.png", dpi=120)
    plt.close()