import cv2
import scipy.ndimage

# Opening the image.
filename = 'input_cir.png'
filename = 'input_vhuman_t1.png'
# filename = 'input_spinwheel.png'
# filename = 'input_maps1.png'
# filename = 'input_laplacian.png'
a = cv2.imread('../Figures/' + filename)

# Converting the image to grayscale.
a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)

# Performing Laplacian filter.
# b = scipy.ndimage.filters.laplace(a,mode='reflect')
b = scipy.ndimage.laplace(a, mode='reflect') # the `scipy.ndimage.filters` namespace is deprecated

cv2.imwrite('../Figures/2.2.1_laplacian_output.png', b)

# CANNOT REPRODUCE FIGURE 4.10 b
