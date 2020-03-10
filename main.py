import os, sys

from utils import *
from tools import *

MAIN = os.path.abspath(os.path.dirname(__file__))
DATA = os.path.join(MAIN, "data")
SOUND = os.path.join(DATA, "P2.5s.wav")

def main():

    file = SOUND
    N = 0.064 # 64 ms
    pas = 0.01 # 10 ms 
    seuilmin = 50
    seuilmax = 500
    if len(sys.argv) == 1 + 5:
        file = sys.argv[1]
        N = int(sys.argv[2])*0.001
        pas = int(sys.argv[3])*0.001
        seuilmin = int(sys.argv[4])
        seuilmax = int(sys.argv[5])
    elif len(sys.argv) == 1: 
        print("usage : <filename> <taille_fenetre> <pas_glissement> <seuilmin> <seuilmax>")
    else:
        print("usage : <filename> <taille_fenetre> <pas_glissement> <seuilmin> <seuilmax>")
        sys.exit()

    signal, params, _, time_step = load_sound(file, p=1)

    fe = params[2]
    N = int(N*fe) # 64 ms * freq echant
    pas = int(pas*fe) # 10 ms * fe

    print("Fréquence fondamentale :")
    mini, maxi, mean = calc_f0(signal, N, pas, time_step, seuilmin = seuilmin, seuilmax = seuilmax)

    print("Mini:", mini, "Hz\nMaxi:", maxi, "Hz\nMean:", mean, "Hz")

if __name__ == "__main__":
    main()