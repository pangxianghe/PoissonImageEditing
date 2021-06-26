import cv2
import numpy as np

# src_path = './images/input/4/source.png'
out_path = './images/input/4/mask.png'

# src = cv2.imread(src_path, cv2.IMREAD_COLOR)
mask = np.zeros((242, 256))
mask[:, 140:] = 255
cv2.imshow('', mask)
cv2.waitKey(0)
cv2.imwrite(out_path, mask)


