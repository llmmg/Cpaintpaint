import numpy as np
import cv2
img = np.zeros((500,500,3), np.uint8)


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
