import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread('./images/test6_src.png')
msk = np.zeros((640, 480))
msk[100:310, 25:280] = 255
cv2.imwrite('./images/test6_mask.png', msk)
plt.imshow(msk)
plt.show()
