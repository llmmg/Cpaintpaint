import numpy as np
import cv2
img = np.zeros((500,500,3), np.uint8)

img[100,101]=[100,4,100]
img[100,102]=[100,4,200]
img[100,110]=[100,4,250]
img[100,120]=[100,4,250]
img[100,130]=[100,4,250]



cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
