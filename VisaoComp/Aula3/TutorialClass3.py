import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import numpy as np
import cv2


plt.close('all')
# ----------------------------------------------------------------
# img = cv2.imread('VisaoComp/Aula3/IMG/python_opencv_gray.png') # Comando para abrir imagem
# imgGREYSCALE =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Conversão de formato default para grayscale
for x in ['python_opencv_gray.png','landscape.jpg','landscape_gray.jpg','python_opencv.png']:
    imgGREYSCALE = cv2.imread('VisaoComp/Aula3/IMG/'
                            + x , 0)  # Comando para abrir imagem se utilizado ,0 no final abre automaticament em greyscale

    # ------------------------------------------------------------------------------------------

    imgGREYSCALEVector = np.array(imgGREYSCALE).flatten()  # Conversão de imagem grayscale em vetor
    plt.figure('Histogram for '+x+' picture') # Cria Imagem em escala de cinzentos

    #Comando plt.hist():
    plt.hist(imgGREYSCALEVector, bins=int(255)) 
    plt.subplot(3, 1, 1), plt.hist(imgGREYSCALEVector, bins=int(255))
    plt.title('Plt.hist() '+x+' histograma')

    #Comando np.histogram():
    hist, bins = np.histogram(imgGREYSCALE, bins='auto')
    plt.subplot(3, 1, 2), plt.plot(hist), plt.title('Np.histogram() '+x+' histograma')
    #Comando plt.histogram():
    hist = cv2.calcHist([imgGREYSCALE], [0], None, [256], [0, 256])
    plt.subplot(3, 1, 3), plt.plot(hist), plt.title('cv2.calcHist() '+x+' histograma')
    # Equalização de figura
    equalizedPicture = cv2.equalizeHist(imgGREYSCALE)
    # Comandos para mostrar figuras não equalizada vs figura equalziada
    plt.figure('Histogram for gray scale picture '+x+' (not equalized vs equalized)') # Cria Imagem em escala de cinzentos
   #Figura não equalizada
    plt.subplot(2,2,1), plt.imshow(imgGREYSCALE, 'gray'), plt.title('cv2.calcHist() histograma')
    plt.subplot(2,2,2), plt.plot(hist), plt.title('cv2.calcHist() '+x+' histograma')
    histEqualized = cv2.calcHist([equalizedPicture], [0], None, [256], [0, 256])
    #Figura equalizada
    plt.subplot(2,2,3), plt.imshow(equalizedPicture, 'gray'), plt.title('Figura '+x+' Equalizada')
    plt.subplot(2,2,4), plt.plot(histEqualized), plt.title('cv2.calcHist() '+x+' histograma equalizada')
plt.show()
