import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,6, 1024);

square_wave_fourier_exp = np.zeros(1024)

K = np.arange(1, 21, 2) # array of = 2k-1
for k in K:
    sinusoid = np.sin(2*np.pi*k*t)
    coefficient = 4/np.pi/k
    square_wave_fourier_exp += coefficient*sinusoid

'''
use loop to stack all layers of approximation when n= k, the sum is the final
fourier exp.
'''

plt.plot(t, square_wave_fourier_exp)

plt.show()
