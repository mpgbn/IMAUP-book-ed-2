# PIL module to read and save an image.
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Opening image and converting it into grayscale.
img = Image.open('sample_1920×1280.png').convert('L')

# convert PIL Image object to numpy array
img = np.array(img)

# We process img_grayscale and obtain img_processed
# The function image_processing can perform any image
# processing or computer vision operation
# img_processed = image_processing(img)

# Converting ndarray to a PIL Image.
# img_out = Image.fromarray(img_processed)
img_out = Image.fromarray(img)

# Save the image to a file.
img_out.save('grayscale_pil.png')


# We import matplotlib.pyplot to display an image in grayscale.
# plt.imshow(img_processed, 'gray')
plt.imshow(img_out, 'gray')
plt.show()