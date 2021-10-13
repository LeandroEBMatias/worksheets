# %%
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import cv2

# Read image
img = cv2.imread('VisaoComp/IMG/python_opencv.png')
# %%
# Output img with window name as 'image'
# cv2.imshow('Image loaded with OpenCV', img)
# # Maintain output window until user presses a key
# cv2.waitKey(0)
# # present windows on screen

#----------------------------------------------------------------
# Converte Imagem  em escala de cinzentos
imgGREYSCALE =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# Converte Imagem  em BRG em RGB
imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# Converte Imagem  em BRG em HSV
imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# Converte Imagem  em BRG em CIELAB
imgCIE = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
#----------------------------------------------------------------
# Converte em array do numpy
imgGREYSCALE = np.array(imgGREYSCALE)
imgRGB = np.array(imgRGB)
imgHSV = np.array(imgHSV)
imgCIE = np.array(imgCIE)
#----------------------------------------------------------------
# Separação em diferentes componenets R, G e B respectivamente
imgR = imgRGB[:,:,0]
imgG = imgRGB[:,:,1]
imgB = imgRGB[:,:,2]
# Subplot de imagens RGB
plt.subplot(2, 2, 1), plt.imshow(imgRGB), plt.title('Imagem RGB') 
plt.subplot(2, 2, 2), plt.imshow(imgR, 'gray'), plt.title('Componente Vermelha')
plt.subplot(2, 2, 3), plt.imshow(imgG, 'gray'), plt.title('Componente Verde')
plt.subplot(2, 2, 4), plt.imshow(imgB, 'gray'), plt.title('Componente Azul')
# Mostra Imagens
plt.show();
#------------------------------------------------------------------------------
# Utilização de Modelo HSV
imgH = imgHSV[:,:,0]
imgS = imgHSV[:,:,1]
imgV = imgHSV[:,:,2]
# Subplot de imagens HSV
plt.subplot(2, 2, 1), plt.imshow(imgHSV), plt.title('Imagem HSV') 
plt.subplot(2, 2, 2), plt.imshow(imgH, 'gray'), plt.title('Componente H')
plt.subplot(2, 2, 3), plt.imshow(imgS, 'gray'), plt.title('Componente S')
plt.subplot(2, 2, 4), plt.imshow(imgV, 'gray'), plt.title('Componente V')
# Mostra Imagens
plt.show();
#------------------------------------------------------------------------------
# Utilização de Modelo CIE
imgC = imgCIE[:,:,0]
imgI = imgCIE[:,:,1]
imgE = imgCIE[:,:,2]
# Subplot de imagens HSV
plt.subplot(2, 2, 1), plt.imshow(imgCIE), plt.title('Imagem CIE') 
plt.subplot(2, 2, 2), plt.imshow(imgH, 'gray'), plt.title('Componente C')
plt.subplot(2, 2, 3), plt.imshow(imgS, 'gray'), plt.title('Componente I')
plt.subplot(2, 2, 4), plt.imshow(imgV, 'gray'), plt.title('Componente E')
# Mostra Imagens
plt.show();
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Exercicio 2.2 
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
treshValue = 127
maxValue = 255
ret, thresh1 = cv2.threshold(imgGREYSCALE,treshValue,maxValue, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(imgGREYSCALE,treshValue,maxValue, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(imgGREYSCALE,treshValue,maxValue, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(imgGREYSCALE,treshValue,maxValue, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(imgGREYSCALE,treshValue,maxValue, cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [imgGREYSCALE, thresh1, thresh2, thresh3, thresh4, thresh5]


for i in range(len(titles)):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
#--------------------------------------------------------------------------------------------
im_flat = np.reshape(img,(img.shape[0]*img.shape[1]))

[hist, _] = np.histogram(img, bins=256, range=(0, 255))
# Normalization so we have probabilities-like values (sum=1)
hist = 1.0*hist/np.sum(hist)

val_max = -999
thr = -1
for t in range(1,255):
    # Non-efficient implementation
    q1 = np.sum(hist[:t])
    q2 = np.sum(hist[t:])
    m1 = np.sum(np.array([i for i in range(t)])*hist[:t])/q1
    m2 = np.sum(np.array([i for i in range(t,256)])*hist[t:])/q2
    val = q1*(1-q1)*np.power(m1-m2,2)
    if val_max < val:
        val_max = val
        thr = t

print("Threshold: {}".format(thr))


plt.subplot(131)
plt.imshow(img, cmap = 'gray')
plt.subplot(132)
plt.hist(im_flat, bins=256, range=(0, 255))
plt.subplot(133)
plt.imshow(img > thr, cmap = 'gray')
plt.show()

cv2.destroyAllWindows()