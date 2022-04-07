import cv2
from scipy import ndimage

# Opening the image.
filename = 'input_cir.png'
# filename = 'input_vhuman_t1.png'
# filename = 'input_spinwheel.png'
# filename = 'input_maps1.png'
# filename = 'input_laplacian.png'
a = cv2.imread('../Figures/' + filename)

# Converting a to grayscale .
a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)

# Performing Prewitt filter.
b = ndimage.prewitt(a)
min_b, max_b = b.min(), b.max()
b = 255.0*(b-min_b)/(max_b-min_b)

# Saving b.
cv2.imwrite('../Figures/2.1.2_prewitt_output.png', b)
