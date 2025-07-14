import cv2
import numpy as np

img = cv2.imread(input("Enter the path to the image: "))
           
--img[:, :, 0]
++img[:, :, 1]

cv2.imshow('Image Window', img)

# Wait for a key press and close the window
cv2.waitKey(0)        # 0 means wait indefinitely
cv2.destroyAllWindows()