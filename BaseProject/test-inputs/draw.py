import numpy as np
import cv2
img = np.zeros((400,300,3), np.uint8)
img[20.0,20.0]=[255.0,255.0,60.0]
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
