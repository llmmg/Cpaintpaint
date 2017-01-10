import numpy as np
import cv2
img = np.zeros((400,300,3), np.uint8)

img[101.0,100.0]=[100.0,4.0,100.0]
img[102.0,100.0]=[100.0,4.0,200.0]
img[110.0,100.0]=[100.0,4.0,250.0]
img[120.0,100.0]=[100.0,4.0,250.0]
img[130.0,100.0]=[100.0,4.0,250.0]



cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
