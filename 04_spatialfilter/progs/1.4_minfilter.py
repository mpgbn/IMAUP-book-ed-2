import cv2
import scipy.ndimage

# opening the image and converting it to grayscale
a = cv2.imread('../Figures/1.3_wave.png')

# performing minimum filter
# b = scipy.ndimage.filters.minimum_filter(a, size=5)
b = scipy.ndimage.minimum_filter(a, size=5) # the `scipy.ndimage.filters` namespace is deprecated

# saving b as mino.png
cv2.imwrite('../Figures/1.4_min_output.png', b)
