import numpy as np

def autocorrelation(signal, N, fe=16000, m=50):
    return [(1 / (N - t)) * np.sum(signal[:-t-1]*np.roll(signal,-t)[:-t-1]) for t in range(int(fe // m))]

def calc_f0_fenetre(signal, N, time_step, fe=16000, m=50, i=32):
    aut = autocorrelation(signal, N, fe, m)
    return 1/((np.argmax(aut[i:-1])+i)*time_step)

def _calc_f0(signal, N, pas, time_step, seuilmin = 50, seuilmax = 500, fe=16000, m=50, i=32):
    for n in range(0, len(signal)-1, pas):
        s = calc_f0_fenetre(signal[n:n+N-1], N, time_step, fe, m, i)
        if s > seuilmin and s < seuilmax :
            yield s

def calc_f0(*args, **kwargs):
    s = [i for i in _calc_f0(*args, **kwargs)]
    return np.min(s), np.max(s), np.mean(s)
        