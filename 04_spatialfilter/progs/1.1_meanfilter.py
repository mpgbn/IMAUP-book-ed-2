import cv2
import numpy as np
import scipy.ndimage

def mask(n):
    m = np.ones((n,n))/(n*n)
    return m

# Opening the image using cv2.
a = cv2.imread('../Figures/1.1_ultrasound_muscle.png')

# Converting the image to grayscale.
a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)

# Initializing the filter of size n by n.
# The filter is divided by nxn for normalization.
n = 7
k = mask(n)

# performing convolution
# b = scipy.ndimage.filters.convolve(a, k) 
b = scipy.ndimage.convolve(a, k) # the `scipy.ndimage.filters` namespace is deprecated

# Writing b to a file.
cv2.imwrite('../Figures/1.1_mean_output_' + str(n) + '.png', b)
