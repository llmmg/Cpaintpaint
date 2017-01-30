import numpy as np
import cv2
img = np.zeros((400,300,3), np.uint8)

img[130,10]=[10,250,250]
img[130,20]=[20,250,250]
img[130,30]=[30,250,250]
img[130,40]=[40,250,250]
img[130,50]=[50,250,250]
img[130,60]=[60,250,250]
img[130,70]=[70,250,250]
img[130,80]=[80,250,250]
img[130,90]=[90,250,250]
img[130,100]=[100,250,250]


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
