import numpy as np
import cv2
img = np.zeros((400,300,3), np.uint8)

img[100.0,100.0]=[1.0,4.0,100.0]


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
