import cv2
from skimage.exposure import equalize_adapthist

img = cv2.imread('../Figures/7_embryo.png')

# Applying Clahe.
img2 = equalize_adapthist(img, clip_limit = 0.01)

# Rescaling img2 from 0 to 255.
img3 = img2*255.0

# Saving img3.
cv2.imwrite('../Figures/7_clahe_output.png', img3)
