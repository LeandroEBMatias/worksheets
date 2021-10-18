import cv2 as cv
# Caminho para a pasta
path = 'Aula4'
# Nome da imagem
imagem = "Leiria"
Noises = ["_noise_Gaussian", "_noise_Poisson", "_noise_Salt_&_Pepper", "_noise_Speckle"]
for Noise in Noises:
    img = cv2.imread(path+"/"+imagem+Noise+".jpg")
    
