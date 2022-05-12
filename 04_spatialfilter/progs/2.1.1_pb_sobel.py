import cv2
from scipy import ndimage

# I. Sobel, G. Feldman, "A 3x3 Isotropic Gradient Operator for Image Processing," presented at a talk at the Stanford Artificial Project in 1968, unpublished but often cited, orig. in Pattern Classification and Scene Analysis, Duda,R. and Hart,P., John Wiley and Sons,'73, pp271-2 (This citation is from Wikipedia)

# Opening the image.
filename = 'input_cir.png'
# filename = 'input_vhuman_t1.png'
# filename = 'input_spinwheel.png'
# filename = 'input_maps1.png'
# filename = 'input_laplacian.png'
a = cv2.imread('../Figures/' + filename)

# Converting a to grayscale .
a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)

# Performing Sobel filter.
b = ndimage.sobel(a)

# Saving b.
cv2.imwrite('../Figures/2.1.1_sobel_output.png', b)
