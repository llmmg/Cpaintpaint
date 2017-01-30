import numpy as np
import cv2
img = np.zeros((400,300,3), np.uint8)

img[101,100]=[100,4,100]
img[102,100]=[100,4,200]
img[110,100]=[100,4,250]
img[120,100]=[100,4,250]
img[130,100]=[100,4,250]



cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
