import numpy as np
import matplotlib.pyplot as plt

# The figsize controls the size of the whole figure, not a single subplot.
fig = plt.figure(figsize = (8,6))

# equivalent but more general
ax1=plt.subplot(2, 2, 1)

# add a subplot with no frame
ax2=plt.subplot(222, frameon=False)

# add a polar subplot
plt.subplot(223, projection='polar')

# add a red subplot that shares the x-axis with ax1
plt.subplot(224, sharex=ax1, facecolor='red')

# delete ax2 from the figure
plt.delaxes(ax2)

# add ax2 to the figure again
plt.subplot(ax2)

plt.show()

import scipy.misc
fig, axes = plt.subplots(2,2, figsize=(8,6));
axes[0,0].imshow(scipy.misc.face())
'''
notice this!
comment: scipy.misc.face() returns a png of a recoon.
'''
axes[0,1]
axes[1,0]
axes[1,1]
plt.show()
