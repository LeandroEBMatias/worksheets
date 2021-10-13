import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import numpy as np
import cv2
# Read image
img = cv2.imread('VisaoComp/Aula3/IMG/python_opencv_gray.png')
imgGREYSCALE =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# plt.imshow(img), plt.title('Imagem')
# plt.show()

# Histograma

# plt.hist(imgGREYSCALE)
# plt.show()

hist, bins = np.histogram(imgGREYSCALE, bins = 'auto')
# plt.plot(imgGREYSCALE.ravel(),256,[0,256])
plt.plot(hist)
plt.title('Histogram for gray scale picture')
plt.show()
# while True:
#     k = cv2.waitKey(0) & 0xFF     
#     if k == 27: break             # ESC key to exit
# cv2.destroyAllWindows()