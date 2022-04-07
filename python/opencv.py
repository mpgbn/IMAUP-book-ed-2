# Open CV module to read and save an image.
import cv2
import matplotlib.pyplot as plt


# Opening image and converting it into grayscale.
img = cv2.imread('sample_1920×1280.png')
img_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



# We process img_grayscale and obtain img_processed.
# The function image_processing can perform any image
# processing or computer vision operation
# img_processed = image_processing(img_grayscale)





# cv2.imwrite will take an ndarray and store it.
# cv2.imwrite('file_name.png', img_processed)
cv2.imwrite('grayscale_opencv.png', img_grayscale)

cv2.imshow(img_grayscale)

# We import matplotlib.pyplot to display an image in grayscale.
# plt.imshow(img_processed, 'gray')
# plt.imshow(img_grayscale, 'gray')
# plt.show()

