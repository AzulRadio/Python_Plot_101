import numpy as np
import matplotlib.pyplot as plt

import scipy.io.wavfile
# Returns 1 second of the piano playing A440, along with the sampling rate
def loadPiano():
    sampling_rate, piano = scipy.io.wavfile.read('piano.wav');
    piano = piano[15000:15000+sampling_rate,0];
    piano = piano/np.linalg.norm(piano);
    t_piano = np.linspace(0, 1, sampling_rate);
    return sampling_rate, t_piano, piano;

# Returns 1 second of the oboe playing A440, along with the sampling rate
def loadOboe():
    sampling_rate, oboe = scipy.io.wavfile.read('oboe.wav');
    oboe = oboe[15000:15000+sampling_rate];
    t_oboe = np.linspace(0, 1, sampling_rate);
    oboe = oboe/np.linalg.norm(oboe);
    return sampling_rate, t_oboe, oboe;

sampling_rate_piano, t_piano, piano = loadPiano();
sampling_rate_oboe, t_oboe, oboe = loadOboe();

fig = plt.figure(figsize = (5,10))

plt.subplot(3,1,1)

plt.plot(t_piano,piano)
plt.plot(t_oboe,oboe)
plt.xlim([0,0.01])

plt.subplot(3,1,2)

w_piano = np.fft.fft(piano);
w_piano = np.fft.fftshift(w_piano);
w = np.fft.fftfreq(sampling_rate_piano, d=1/sampling_rate_piano)
w = np.fft.fftshift(w);
plt.ylim([0,40])
plt.xlim([0, 4000])
plt.plot(w,np.abs(w_piano))


plt.subplot(3,1,3)

w_oboe = np.fft.fft(oboe);
w_oboe = np.fft.fftshift(w_oboe);
w = np.fft.fftfreq(sampling_rate_oboe, d=1/sampling_rate_oboe)
w = np.fft.fftshift(w);
plt.ylim([0,30])
plt.xlim([0, 4000])
plt.plot(w,np.abs(w_oboe))

plt.show()
