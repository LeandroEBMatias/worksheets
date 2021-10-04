# #%%
# #--------------------------------------------------------------------------------------------------
# #  4.1 Desenhar a Curva
# #--------------------------------------------------------------------------------------------------

# import libraries
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
# define 100 points in [0,1] interval
t = np.linspace(0, 1, 100)
t = sp.linspace(0, 1, 100)
# plot a parabola curve in the defined interval
plt.plot(t, t**2)
plt.show()

# #%%
# #--------------------------------------------------------------------------------------------------
# # 4.2 Abrir e Mostrar Projeto com biblioteca OpenCV 
# #--------------------------------------------------------------------------------------------------
import cv2

# Read image
img = cv2.imread('python_opencv.png')

# Output img with window name as 'image'
cv2.imshow('Image loaded with OpenCV', img)
# Maintain output window until user presses a key
cv2.waitKey(0)
# present windows on screen
cv2.destroyAllWindows()

# #%%
# #--------------------------------------------------------------------------------------------------
# # 4.3 Abrir e Mostrar Imagem com biblioteca matplotlib 
# #--------------------------------------------------------------------------------------------------

# importing matplotlib modules
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# Read image
img = mpimg.imread('python_opencv.png')

# Output Images
plt.imshow(img)
# Maintains the output window visible
plt.show()



#--------------------------------------------------------------------------------------------------
# 4.4 Abrir modificar e salvar resultado numa nova imagem
#--------------------------------------------------------------------------------------------------

# importing OpenCV(cv2) module
# import cv2
# # Read image
# image = cv2.imread('python_opencv.png')
# # Converts to grayscale
# image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# # Saves the resulting image
# cv2.imwrite('python_opencv_gray.png', image_gray)
# # Outputs the images
# cv2.imshow('Original image', image)
# cv2.imshow('Gray image', image_gray)
# # Maintain output window until user presses a key
# cv2.waitKey(0)
# # present windows on screen
# cv2.destroyAllWindows()
