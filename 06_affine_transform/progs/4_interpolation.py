# import numpy as np
# import scipy.misc, math
# from scipy.misc.pilutil import Image
from skimage.transform import AffineTransform, warp
import cv2
from matplotlib import pyplot as plt

# img = Image.open('../Figures/angiogram1.png').convert('L')
# img1 = scipy.misc.fromimage(img)

img1 = cv2.imread('../Figures/angiogram1.png')

transformation = AffineTransform(scale=(0.3, 0.3))

# nearest neighbor order = 0
img2 = warp(img1, transformation, order=0)
# im4 = scipy.misc.toimage(img2)
# im4.save('../Figures/interpolate_nn_output.png')
# im4.show()

# bi-linear order = 1
img3 = warp(img1, transformation, order=1) # default
# im4 = scipy.misc.toimage(img2)
# im4.save('../Figures/interpolate_bilinear_output.png')
# im4.show()

#bi-quadratic order = 2
img4 = warp(img1, transformation, order=2)
# im4 = scipy.misc.toimage(img2)
# im4.save('../Figures/interpolate_biquadratic_output.png')
# im4.show()

#bi-cubic order = 3
img5 = warp(img1, transformation, order=3)
# im4 = scipy.misc.toimage(img2)
# im4.save('../Figures/interpolate_bicubic_output.png')
# im4.show()

# create figure
fig = plt.figure()

# setting values to rows and column variables
rows = 2
columns = 2

# Adds a subplot at the 1st position
fig.add_subplot(rows, columns, 1)
  
# showing image
plt.imshow(img2)
plt.axis('off')
plt.title("nearest neighbor order = 0")
  
# Adds a subplot at the 2nd position
fig.add_subplot(rows, columns, 2)
  
# showing image
plt.imshow(img4)
plt.axis('off')
plt.title("bi-linear order = 1")

# Adds a subplot at the 3rd position
fig.add_subplot(rows, columns, 3)
  
# showing image
plt.imshow(img4)
plt.axis('off')
plt.title("bi-quadratic order = 2")
  
# Adds a subplot at the 4th position
fig.add_subplot(rows, columns, 4)
  
# showing image
plt.imshow(img5)
plt.axis('off')
plt.title("bi-cubic order = 3")

plt.show()