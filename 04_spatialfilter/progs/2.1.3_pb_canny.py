import cv2
 
# Opening the image.
filename = 'input_cir.png'
# filename = 'input_vhuman_t1.png'
# filename = 'input_spinwheel.png'
# filename = 'input_maps1.png'
# filename = 'input_laplacian.png'
a = cv2.imread('../Figures/' + filename)

# Converting the image to grayscale.
a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)

# Performing Canny edge filter.
b = cv2.Canny(a, 100, 200)

# Saving b.
cv2.imwrite('../Figures/2.1.3_canny_output.png', b) 
