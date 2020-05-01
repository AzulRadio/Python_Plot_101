import numpy as np
import matplotlib.pyplot as plt

fs=8000.0;
f_1=500.0; phase_1=0
f_2=750.0; phase_2=np.pi/4.0
f_3=1500.0; phase_3=np.pi/2.0
f_4=4500.0; phase_4=0; 
t=np.arange(0,1,1/fs)
y=1
y=y+np.cos(2*np.pi*f_1*t+phase_1)
y=y+0.5*np.cos(2*np.pi*f_2*t+phase_2)
y=y+np.cos(2*np.pi*f_3*t+phase_3)
y=y+np.cos(2*np.pi*f_4*t+phase_4)
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 4))
axes[0].plot(t[0:80],y[0:80],'r.-') # Plot signal in time
axes[0].set_xlabel('Time (seconds)')
axes[0].set_ylabel('Amplitude')
axes[0].set_title('Time domain')

N=1024;
y_spec=np.fft.fft(y,N)
y_spec=np.fft.fftshift(y_spec)
ff=np.linspace(-fs/2,fs/2,N) # Frequency axis
y_spec_mag=abs(y_spec) #Plot signal in frequency domain
y_spec_phase=np.angle(y_spec)

axes[1].plot(ff,y_spec_mag,'r')
axes[1].set_xlabel('frequency')
axes[1].set_ylabel('magnitude')
axes[1].set_title('Fourier Transform')

fig.tight_layout()
plt.show()

'''
Notice: fft assume the function is periodic!!!
So the length of time windowing may affect the freq domain
'''
