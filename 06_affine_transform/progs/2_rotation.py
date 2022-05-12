# import numpy as np
# import scipy.misc, math
# from scipy.misc.pilutil import Image
from skimage.transform import AffineTransform, warp
import cv2
from matplotlib import pyplot as plt

# img = Image.open('../Figures/angiogram1.png').convert('L')
# img1 = scipy.misc.fromimage(img)

img1 = cv2.imread('../Figures/angiogram1.png')

# rotation angle in radians (pi radians = 180 degrees)
transformation = AffineTransform(rotation=0.1)
img2 = warp(img1, transformation)
# im4 = scipy.misc.toimage(img2)
# im4.save('../Figures/rotate_output.png')
# im4.show()

plt.imshow(img2, interpolation='nearest')
plt.show()
