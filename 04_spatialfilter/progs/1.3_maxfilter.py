import scipy.misc
import scipy.ndimage
from PIL import Image

# opening the image and converting it to grayscale
a = Image.open('../Figures/1.3_wave.png').convert('L')

# performing maximum filter
# b = scipy.ndimage.filters.maximum_filter(a, size=5)
b = scipy.ndimage.maximum_filter(a, size=5) # the `scipy.ndimage.filters` namespace is deprecated

# b is converted from an ndarray to an image
# b = scipy.misc.toimage(b)
# b.save('../Figures/1.3_max_output.png')

# Saving b as png image in Figures folder
img_out = Image.fromarray(b)
img_out.save('../Figures/1.3_max_output.png')
