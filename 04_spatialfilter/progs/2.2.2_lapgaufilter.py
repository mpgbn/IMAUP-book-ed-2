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

# Performing Laplacian of Gaussian.
# b = scipy.ndimage.filters.gaussian_laplace(a, sigma=1, mode='reflect')
b = scipy.ndimage.gaussian_laplace(a, sigma=1, mode='reflect') # the `scipy.ndimage.filters` namespace is deprecated

cv2.imwrite('../Figures/2.2.2_log_output.png', b)