import numpy as np
import matplotlib.pyplot as plt
import scipy.misc

def visualizeColorChannels(red, green, blue):
    emptyChannel = np.zeros(red.shape)
    fig, axes = plt.subplots(1,3, figsize=(20,10))
    axes[0].imshow(np.stack((red, emptyChannel, emptyChannel), axis=-1).astype(int))
    axes[1].imshow(np.stack((emptyChannel, green, emptyChannel), axis=-1).astype(int))
    axes[2].imshow(np.stack((emptyChannel, emptyChannel, blue), axis=-1).astype(int))


# Imports an example RGB image of a raccoon
image = scipy.misc.face()
'''
This function just returns a picture of a racoon. 
'''
if (image.dtype != int):
    image.astype(int)
if (np.max(image) <= 1):
    image *= 256
print(image.shape, '<- The array shape is height x width x color')
plt.imshow(image)

# Enter your code below to get red, green, and blue channels
red =   image[::,::,0] # Replace assignment with your code to get red-channel subarray here
green = image[::,::,1] # Replace assignment with your code to get green-channel subarray here
blue =  image[::,::,2] # Replace assignment with your code to get blue-channel subarray here

grayscale = 0.21*red + 0.71*green + 0.08*blue
'''
We get this by the grayscale formula.
'''

plt.imshow(grayscale, cmap = 'gray')

visualizeColorChannels(red, green, blue)

hisgram = np.ravel(image)
'''
np.ravel is to flatten a multi-array to a 1-d array, so we can plot it with
plt.hist
'''


fig, axes = plt.subplots(1,1, figsize=(10,5))

axes = plt.hist(hisgram, bins = 256);

plt.show()




'''
This is how the "image" looks like:
Its shape is (768, 1024, 3), meaning it's a 768*1024 2-d array,
but every element is an array with 3 elements.

[[[121 112 131]
  [138 129 148]
  [153 144 165]
  ...
  [119 126  74]
  [131 136  82]
  [139 144  90]]

 [[ 89  82 100]
  [110 103 121]
  [130 122 143]
  ...
  [118 125  71]
  [134 141  87]
  [146 153  99]]

 ...


 [[ 85 101  74]
  [ 97 113  84]
  [111 126  97]
  ...
  [120 156  95]
  [119 155  93]
  [118 154  92]]]
'''
