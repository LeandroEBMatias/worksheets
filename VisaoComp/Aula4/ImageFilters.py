import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

# Função utilizada para primeira alinea

# Realização de filtro de média


def alinea_a(Noises, imagem, path, imageList, bluredImageList, boxFilterImageList, ksizes):
    for Noise in Noises:
        figure = imagem+Noise
        img = cv.imread(path+"/"+figure+".jpg")
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        imageList.append(img)
        for ksize in ksizes:
            img_blur = cv.blur(img, ksize)
            img_boxFilter = cv.boxFilter(img, -1, ksize)
            bluredImageList.append(img_blur)
            boxFilterImageList.append(img_boxFilter)
            plt.figure(figure + ' blured '+'ksize ' +
                       str(ksize[0])+" "+str(ksize[1]))
            plt.subplot(1, 2, 1), plt.imshow(img)
            plt.subplot(1, 2, 2), plt.imshow(img_blur)
            plt.figure(figure + ' box_Filter '+'ksize ' +
                       str(ksize[0])+" "+str(ksize[1]))
            plt.subplot(1, 2, 1), plt.imshow(img)
            plt.subplot(1, 2, 2), plt.imshow(img_boxFilter)


# ------------------------------------------------------------------------------
# Caminho para a pasta
path = 'VisaoComp/Aula4'
# Nome da imagem
imagem = "Leiria"
# Ruidos associados às imagens
Noises = ["_noise_Gaussian", "_noise_Poisson",
          "_noise_Salt_&_Pepper", "_noise_Speckle"]
# ----------------------------------------------------------------
# Variáveis Alinea A
imageList = []
bluredImageList = []
boxFilterImageList = []
ksizes = [(3, 3), (50, 50)]
# -----------------------------------------------------------------
# Variaveis Alinea B
kernel_size = 3
kernel = np.array([[0, 0, 0],
                  [0, 0, 1],
                  [0, 0, 0]])

# -----------------------------------------------------------------
# alinea_a(Noises,imagem,path, imageList, bluredImageList,boxFilterImageList,ksizes)

img = cv.imread(path+"/"+imagem+"_gray"+".jpg", 0)
kernelFilterTest = cv.filter2D(img, -1, kernel)
plt.subplot(1, 2, 1), plt.imshow(img, 'gray')
plt.subplot(1, 2, 2), plt.imshow(kernelFilterTest, 'gray')
# img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.show()
