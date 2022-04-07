import cv2
from skimage import filters
from scipy import ndimage

# I. Sobel, G. Feldman, "A 3x3 Isotropic Gradient Operator for Image Processing," presented at a talk at the Stanford Artificial Project in 1968, unpublished but often cited, orig. in Pattern Classification and Scene Analysis, Duda,R. and Hart,P., John Wiley and Sons,'73, pp271-2 (This citation is from Wikipedia)

# ***** FUNCTION NOT IN ORIGINAL CODE! *****
def grayscale(data):
    min, max = data.min(), data.max()
    out = 255*(data-min)/(max-min)
    return out

# Opening the image.
filename = 'input_cir.png'
# filename = 'input_vhuman_t1.png'
# filename = 'input_spinwheel.png'
# filename = 'input_maps1.png'
# filename = 'input_laplacian.png'
a = cv2.imread('../Figures/' + filename)

# Converting a to grayscale.
a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)

# Performing vertical Sobel.
b = filters.sobel_v(a)
min_b, max_b = b.min(), b.max()
b = 255*(b-min_b)/(max_b-min_b)
b = grayscale(b) # modification

# Saving to image
cv2.imwrite('../Figures/2.1.1_sobel_output_v.png', b)

# ***** CODES BELOW NOT IN ORIGINAL CODE! *****

# Performing horizontal Sobel. NOT IN ORIGINAL CODE!
c = filters.sobel_h(a)
c = grayscale(c)

# Saving to image
cv2.imwrite('../Figures/2.1.1_sobel_output_h.png', c)

# Performing Sobel filter from vertical Sobel.
vp = ndimage.sobel(b)

# Performing Sobel filter from horizontal Sobel.
c = ndimage.rotate(c, 90) # modification
hp = ndimage.sobel(c)
hp = ndimage.rotate(hp, -90) # modification

# Saving to images
cv2.imwrite('../Figures/2.1.1_sobel_output_v_p.png', vp)
cv2.imwrite('../Figures/2.1.1_sobel_output_h_p.png', hp)

# Blend vp and hp
vhp = vp + hp
cv2.imwrite('../Figures/2.1.1_sobel_output_vhp.png', vhp)
