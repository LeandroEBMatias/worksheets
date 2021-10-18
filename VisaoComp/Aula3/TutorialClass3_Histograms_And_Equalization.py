import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import numpy as np
import cv2


def rgbHistogram(imageRGB):
    chans = cv2.split(imageRGB)
    colors = ("r", "g", "b")
    i = 0
    for (chan, color) in zip(chans, colors):
        i = i + 1
        plt.subplot(3, 1, i)
        # create a histogram for the current channel and plot it
        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
        plt.title('Histograma Canal: '+color+'not equalized')


# ----------------------------------------------------------------
# img = cv2.imread('VisaoComp/Aula3/IMG/python_opencv_gray.png') # Comando para abrir imagem
# imgGREYSCALE =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Conversão de formato default para grayscale
#------------------------------------------------------------------------------
# for x in ['python_opencv_gray.png', 'landscape_gray.jpg']:
#     imgGREYSCALE = cv2.imread('VisaoComp/Aula3/IMG/'
#                               + x, 0)  # Comando para abrir imagem se utilizado ,0 no final abre automaticament em greyscale

#     # ------------------------------------------------------------------------------------------

#     # Conversão de imagem grayscale em vetor
#     imgGREYSCALEVector = np.array(imgGREYSCALE).flatten()
#     # Cria Imagem em escala de cinzentos
#     plt.figure('Histogram for '+x+' picture')

#     # Comando plt.hist():
#     plt.hist(imgGREYSCALEVector, bins=int(255))
#     plt.subplot(3, 1, 1), plt.hist(imgGREYSCALEVector, bins=int(255))
#     plt.title('Plt.hist() '+x+' histograma')

#     # Comando np.histogram():
#     hist, bins = np.histogram(imgGREYSCALE, bins='auto')
#     plt.subplot(3, 1, 2), plt.plot(hist), plt.title(
#         'Np.histogram() '+x+' histograma')
#     # Comando plt.histogram():
#     hist = cv2.calcHist([imgGREYSCALE], [0], None, [256], [0, 256])
#     plt.subplot(3, 1, 3), plt.plot(hist), plt.title(
#         'cv2.calcHist() '+x+' histograma')
#     # Equalização de figura
#     equalizedPicture = cv2.equalizeHist(imgGREYSCALE)
#     # Comandos para mostrar figuras não equalizada vs figura equalziada
#     # Cria Imagem em escala de cinzentos
#     plt.figure('Histogram for gray scale picture ' +
#                x+' (not equalized vs equalized)')
#    # Figura não equalizada
#     plt.subplot(2, 2, 1), plt.imshow(
#         imgGREYSCALE, 'gray'), plt.title('cv2.calcHist() histograma')
#     plt.subplot(2, 2, 2), plt.plot(hist), plt.title(
#         'cv2.calcHist() '+x+' histograma')
#     histEqualized = cv2.calcHist(
#         [equalizedPicture], [0], None, [256], [0, 256])
#     # Figura equalizada
#     plt.subplot(2, 2, 3), plt.imshow(equalizedPicture,
#                                      'gray'), plt.title('Figura '+x+' Equalizada')
#     plt.subplot(2, 2, 4), plt.plot(histEqualized), plt.title(
#         'cv2.calcHist() '+x+' histograma equalizada')
#-------------------------------------------------------------------------------    

for x in [ 'landscape.jpg','python_opencv.png']:
    img = cv2.imread('VisaoComp/Aula3/IMG/'
                     + x)  # Comando para abrir imagem se utilizado ,0 no final abre automaticament em greyscale
    # Conversão de formato default para RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.figure('Histogram for ' +x +' picture')

    rgbHistogram(imgRGB)

    equalizedPictureRGB = np.zeros(np.shape(np.array(imgRGB)))

    for i in range(2):
        equalizedPictureRGB[:,:,i] = cv2.equalizeHist(imgRGB[:, :, i])
    plt.figure(x + ' picture not-equalized vs equalized')
    plt.subplot(1, 2, 1), plt.imshow(imgRGB)
    plt.subplot(1, 2, 2), plt.imshow(equalizedPictureRGB)
    chans = cv2.split(equalizedPictureRGB)
    plt.figure('hist '+x + ' picture not-equalized vs equalized')
    rgbHistogram(equalizedPictureRGB)
plt.show()
