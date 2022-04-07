from fileinput import filename
import cv2
from skimage import filters
from scipy import ndimage

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

# Converting a to grayscale .
a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)

# Performing vertical Prewitt.
b = filters.prewitt_v(a)
min_b, max_b = b.min(), b.max()
b = 255*(b-min_b)/(max_b-min_b)
b = grayscale(b)

# Saving to image
cv2.imwrite('../Figures/2.1.2_prewitt_output_v.png', b)

# ***** CODES BELOW NOT IN ORIGINAL CODE! *****

# Performing horizontal Prewitt. NOT IN ORIGINAL CODE!
c = filters.prewitt_h(a)
c = grayscale(c)

# Saving to image
cv2.imwrite('../Figures/2.1.2_prewitt_output_h.png', c)

# Performing Prewitt filter from vertical Prewitt.
vp = ndimage.prewitt(b)

# Performing Prewitt filter from horizontal Prewitt.
c = ndimage.rotate(c, 90) # modification
hp = ndimage.prewitt(c)
hp = ndimage.rotate(hp, -90) # modification

# Saving to images
cv2.imwrite('../Figures/2.1.2_prewitt_output_v_p.png', vp)
cv2.imwrite('../Figures/2.1.2_prewitt_output_h_p.png', hp)

# Blend vp and hp
vhp = vp + hp
cv2.imwrite('../Figures/2.1.2_prewitt_output_vhp.png', vhp)


