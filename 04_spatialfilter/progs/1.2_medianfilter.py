import cv2
import scipy.ndimage

# Opening the image and converting it to grayscale.
a = cv2.imread('../Figures/1.2_ct_saltandpepper.png')

# Converting the image to grayscale.
a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)

# Performing the median filter.
# b = scipy.ndimage.filters.median_filter(a, size=5)
b = scipy.ndimage.median_filter(a, size=5) # the `scipy.ndimage.filters` namespace is deprecated

# Saving b as median_output.png in Figures folder
cv2.imwrite('../Figures/1.2_median_output.png', b)
