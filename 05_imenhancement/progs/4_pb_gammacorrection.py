import cv2
import matplotlib.pyplot as plt
import numpy as np

# Opening the image.
a = cv2.imread('../Figures/4_angiogram1.png')

# gamma is initialized.
gamma = 1.5

# b is converted to type float.
b1 = a.astype(float)

# Maximum value in b1 is determined.
b3 = np.max(b1)

# b1 is normalized 
b2 = b1/b3

# gamma-correction exponent is computed.
# b4 = np.log(b2)*gamma # RuntimeWarning: divide by zero encountered in log
result = np.where(b2 > 0.0000000000001, b2, -10)
b4 = np.log(result, out=result, where=result > 0)*gamma

# gamma-correction is performed.
c = np.exp(b4)*255.0

# c is converted to type int.
c1 = c.astype(int)

# Displaying c1
plt.imshow(c1)
plt.show()
