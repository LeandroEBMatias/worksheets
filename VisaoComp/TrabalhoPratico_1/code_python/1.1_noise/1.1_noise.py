# #%%
# #--------------------------------------------------------------------------------------------------
# #  1.1 Nosie Removal
# #--------------------------------------------------------------------------------------------------
# Método usado presente em:
# https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_photo/py_non_local_means/py_non_local_means.html
#----------------------------------------------------------------
# from : https://www.geeksforgeeks.org/python-denoising-of-colored-images-using-opencv/
# Syntax: cv2.fastNlMeansDenoisingColored( P1, P2, float P3, float P4, int P5, int P6)

# Parameters:
# P1 – Source Image Array
# P2 – Destination Image Array
# P3 – Size in pixels of the template patch that is used to compute weights.
# P4 – Size in pixels of the window that is used to compute a weighted average for the given pixel.
# P5 – Parameter regulating filter strength for luminance component.
# P6 – Same as above but for color components // Not used in a grayscale image.
#----------------------------------------------------------------

# import libraries
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import cv2 as cv



# Generalização de variáveis para abrir fotos
grupo = '02'
path = 'VisaoComp/TrabalhoPratico_1/data/'
trabalho = 'noise'
# Abrir imagem
ksize = (3, 3)
img = cv.imread(path+'img'+grupo+'_noise.jpg')
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
img_blur = cv.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
img=cv.cvtColor(img, cv.COLOR_BGR2RGB)
img_blur=cv.cvtColor(img_blur, cv.COLOR_BGR2RGB)
plt.window('fastNlMeansDenoisingColored')
plt.subplot(121),plt.imshow(img)
plt.subplot(122),plt.imshow(img_blur)
plt.show()