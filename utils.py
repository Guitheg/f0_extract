from scipy.io.wavfile import read
import wave
import numpy as np

import matplotlib.pyplot as plt

def normalize(data):
    return data / np.max(np.abs(data), axis=0)

def load_sound(path, interval=(0,-1), p = 0):
    _, data = read(path)
    stream = wave.open(path)
    params = stream.getparams()
    data = np.asarray(data)[interval[0]:interval[1]]
    if p != 0:
        data = normalize(data)*p
    time_step = 1 / params[2] # params[2] = framerate
    duree = data.size / params[2] # params[2] = framerate
    stream.close()
    return data, params, duree, time_step

def plot_n_signal(data, y=None):
    n_data = len(data)
    figure, axes = plt.subplots(n_data, 1)
    if y:
        n_y = len(y)
        if n_y != n_data:
            raise Exception("len(y) ["+str(n_y)+"] != len(data) ["+str(n_data)+"]" ) 

        if n_data > 1:
            for signal, py, ax in zip(data, y, axes) :
                    ax.plot(py, signal)
        else:
            axes.plot(y[0], data[0])
    else :
        if n_data > 1:
            for signal, ax in zip(data, axes) :
                    ax.plot(signal)
        else:
            axes.plot(data[0])
    plt.show()