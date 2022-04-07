import cv2
import numpy as np
from skimage.filters import frangi

filename = 'input_angiogram1.png'
img = cv2.imread('../Figures/' + filename)

# Converting the image to grayscale. MISSING IN ORIGINAL CODE!
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img1 = np.asarray(img)

img2 = frangi(img1, black_ridges=True)

img3 = 255*(img2-np.min(img2))/(np.max(img2)-np.min(img2))

cv2.imwrite('../Figures/3.1_frangi_output.png', img3)

# ENHANCE WITH gThumb!
