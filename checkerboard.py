import cv2
import numpy as np

checker=np.zeros([320,320],dtype='uint8')

for i in range(40,320,80):
    for j in range(40,320,80):
        checker[i-40:i,j-40:j]=255
        checker[i:i+40,j:j+40]=255

cv2.imshow('8*8 checker board',checker)
cv2.waitKey(0)
cv2.destroyAllWindows()
