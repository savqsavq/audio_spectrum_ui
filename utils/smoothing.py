import numpy as np

def moving_avg(arr, n=10):
    if n <= 1:
        return arr
    cumsum = np.cumsum(np.insert(arr, 0, 0))
    return (cumsum[n:] - cumsum[:-n]) / float(n)