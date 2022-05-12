import cv2

# Opening the image.
# im = cv2.imread('../Figures/6_hequalization_input.png')
im = cv2.imread('../Figures/5_bse.png')

# Finding the maximum and minimum pixel values
b = im.max()
a = im.min()
print(a,b)

# Converting im1 to float.
c = im.astype(float)

# Contrast stretching transformation.
im1 = 255.0*(c-a)/(b-a+0.0000001)

# Saving im2 as contrast_output.png in Figures folder 
cv2.imwrite('../Figures/8_contrast_output2.png', im1) 