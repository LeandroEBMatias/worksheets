# -----------------------------------------------------------------
# Import de bibliotecas
# -----------------------------------------------------------------
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
# -----------------------------------------------------------------
# Função utilizada para primeira alinea
# -----------------------------------------------------------------
# Realização de filtro de média
# -----------------------------------------------------------------


def alinea_a(Noises, imagem, path, imageList, bluredImageList, boxFilterImageList, mediamBluredImageList, ksizes):
    for Noise in Noises:
        figure = imagem+Noise
        img = cv.imread(path+"/"+figure+".jpg")
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        imageList.append(img)
        for ksize in ksizes:
            img_blur = cv.blur(img, ksize)
            img_boxFilter = cv.boxFilter(img, -1, ksize)
            img_medianBlur = cv.medianBlur(img, int(ksize[1]))

            bluredImageList.append(img_blur)
            boxFilterImageList.append(img_boxFilter)
            mediamBluredImageList.append(img_medianBlur)

            plt.figure(figure + ' blured '+'ksize ' +
                       str(ksize[0])+" "+str(ksize[1]))
            plt.subplot(3, 2, 1), plt.imshow(img)
            plt.subplot(3, 2, 2), plt.imshow(img_blur)
            # plt.figure(figure + ' box_Filter '+'ksize ' +
            #            str(ksize[0])+" "+str(ksize[1]))
            plt.subplot(3, 2, 3), plt.imshow(img)
            plt.subplot(3, 2, 4), plt.imshow(img_boxFilter)
            # plt.figure(figure + ' Median_blur '+'ksize ' +
            #            str(ksize[0])+" "+str(ksize[1]))
            plt.subplot(3, 2, 5), plt.imshow(img)
            plt.subplot(3, 2, 6), plt.imshow(img_medianBlur)
        plt.show()
# -----------------------------------------------------------------


def alinea_b_c(path, imagem, kernelSide, KernelSideCollum):
    # Abrir imagem
    img = cv.imread(path+"/"+imagem+"_gray"+".jpg", 0)
    # Aplicação de filtros com kernels defenidos manualmente
    # filtro com ponto num dos lados a 1 desloca imagem para lado oposto ao um na matriz
    kernelFilterTestR = cv.filter2D(img, -1, kernelSide)
    # filtro com pontos a um numa das colonas desloca imagem para lado oposto
    # à coluna na matriz e aplica filtro de
    kernelFilterTestRCollum = cv.filter2D(img, -1, KernelSideCollum)
    plt.figure()
    plt.subplot(1, 3, 1), plt.imshow(img, 'gray')
    plt.subplot(1, 3, 2), plt.imshow(kernelFilterTestR, 'gray')
    plt.subplot(1, 3, 3), plt.imshow(kernelFilterTestRCollum, 'gray')
    plt.show()


def alinea_d(imagem, kernel_d_1, kernel_d_2):
    imgOG = cv.imread(path+"/"+imagem+"_gray"+".jpg", 0)
    # Aplicação de filtros com kernels defenidos manualmente
    # filtro com ponto num dos lados a 1 desloca imagem para lado oposto ao um na matriz
    imgList = []
    kernels = [kernel_d_1, kernel_d_2]
    # plt.subplot(2, 2, 1),
    plt.figure()
    plt.imshow(imgOG, 'gray')
    for kernel in kernels:
        imgF = cv.filter2D(imgOG, -1, kernel)
        imgList.append(imgF)
    imgF = imgList[0]-imgList[1]
    # plt.subplot(2, 2, 2)
    plt.figure()
    plt.imshow(imgF, 'gray')
    imgF = cv.filter2D(imgOG, -1, (kernel_d_1-kernel_d_2))
    # plt.subplot(2, 2, 3)
    plt.figure()
    plt.imshow(imgF, 'gray')
    plt.show()


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
mediamBluredImageList = []
ksizes = [(3, 3), (51, 51)]
# -----------------------------------------------------------------
# Variaveis Alinea B
kernel_size = 3
# -----------------------------------------------------------------
# Kernels a implementar nas diferentes funções
# -----------------------------------------------------------------
kernelL = np.array([[0, 0, 0],
                    [1, 0, 0],
                    [0, 0, 0]])
# -----------------------------------------------------------------
kernelLCollum = np.array([[1, 0, 0],
                          [1, 0, 0],
                          [1, 0, 0]])
# -----------------------------------------------------------------
kernelR = np.array([[0, 0, 0],
                    [0, 0, 1],
                    [0, 0, 0]])
# -----------------------------------------------------------------
kernelRCollum = np.array([[0, 0, 1],
                          [0, 0, 1],
                          [0, 0, 1]])
# -----------------------------------------------------------------
kernelRCollum = np.array([[0, 0, 1],
                          [0, 0, 1],
                          [0, 0, 1]])

kernel_d_1 = np.array([[0, 0, 0],
                       [0, 2, 0],
                       [0, 0, 0]])

kernel_d_2 = (1/9) * np.array([[1, 1, 1],
                               [1, 1, 1],
                               [1, 1, 1]])

# kernel_d_1 = np.array([[0, 0, 0],
#                        [0, 4, 0],
#                        [0, 0, 0]])
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# Aliea A filtros de desfoque de mediana e media
# alinea_a(Noises,imagem,path, imageList, bluredImageList,alinea_b_c(path, imagem, kernelSide, KernelSideCollum)
# alinea_b_c(path, imagem, kernelSide, KernelSideCollum)
# alinea_d(imagem, kernel_d_1,kernel_d_2)
ksize = 5
sigma = 1
img = cv.imread(path+"/"+imagem+"_gray"+".jpg", 0)
# ------------------------------------------------------------------------------

# a=cv.getGaussianKernel(ksize, sigma)
# # ksize - kernel size, should be odd and positive (3,5,...)
# # sigma - Gaussian standard deviation. If it is non-positive, it is computed from ksize as sigma = 0.3*((ksize-1)*0.5 - 1) + 0.8
# # ktype - Type of filter coefficients (Optional)
# imgGaussianFiltered = cv.GaussianBlur(imgOG,-1,a, cv.BORDER_DEFAULT)
# plt.imshow(imgGaussianFiltered, 'gray')
# plt.show()
# -----------------------------------------------------------------
# -----------------------------------------------------------------
laplacian = cv.Laplacian(img, cv.CV_64F)
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)
sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)
plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
# compute a "wide", "mid-range", and "tight" threshold for the edges
# using the Canny edge detector
plt.figure()
plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
wide = cv.Canny(img, 10, 200)
plt.subplot(2, 2, 2), plt.imshow(wide, cmap='gray')
mid = cv.Canny(img, 30, 150)
plt.subplot(2, 2, 3), plt.imshow(mid, cmap='gray')
tight = cv.Canny(img, 240, 250)
plt.subplot(2, 2, 4), plt.imshow(tight, cmap='gray')
plt.show()
