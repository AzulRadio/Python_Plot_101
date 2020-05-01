import numpy as np
import matplotlib.pyplot as plt

#1
ff = np.linspace(-8000,8000,1024)

H = np.ones(1024)

H[ff>2000] = 0
H[ff<-2000]  = 0 

'''
Broadcasting can depend on another array as long as their length are the same.
'''

#2
'''
astronaut = plt.imread('astronaut.png');
camera = plt.imread('camera.png');

how to import pictures to analyse
'''

#3

y = np.sin(2*np.pi*np.arange(0, 1, 1/1000))
t = np.arange(0, 1, 1/1000)
fig, ax = plt.subplots(nrows=1, ncols=1)
y_corr = np.correlate(y,y,"full")
y_corr = y_corr[y_corr.size//2:]
'''
notice size of the array is half
'''
ax.plot(t, y_corr, 'b--')
ax.set_xlabel('t')
ax.set_ylabel('y_corr(t)')
ax.set_title('output auto-correlation')

fig.tight_layout()
plt.show()

'''
autocorrelation
'''

#4
'''
np.convolve()
'''
