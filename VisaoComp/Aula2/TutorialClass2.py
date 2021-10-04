# 
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import cv2

# Read image
img = cv2.imread('VisaoComp/IMG/python_opencv_gray.png')

# Output img with window name as 'image'
cv2.imshow('Image loaded with OpenCV', img)
# Maintain output window until user presses a key
cv2.waitKey(0)
# present windows on screen
cv2.destroyAllWindows()