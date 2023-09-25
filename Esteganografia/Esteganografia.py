import cv2
import numpy as np 
import os
from google.colab.patches import cv2_imshow

def esteganografia():
  for i in range(1,4):
    #Identificar as imagens que serão usadas
    img_gato = cv2.imread(f'/content/drive/MyDrive/gatos/gato{i}.png')
    img_cao = cv2.imread(f'/content/drive/MyDrive/Cachorros/cachorro{i}.png')

    #mostrando as imagens originais
    print(f'Imagem GATO{i}:')
    cv2_imshow(img_gato)
    print(f'Imagem CACHORRO{i}:')
    cv2_imshow(img_cao)

    #novas imagens que serão criadas
    nova_img = np.zeros(img_gato.shape, img_gato.dtype)
    img_gato = img_gato & 0b11110000
    nova_img = img_gato | img_cao >> 4

    #caminho do diretorio onde as imagem guardadas
    os.chdir('/content/drive/MyDrive/Esteganografia')

    #salvando a imagens criadas
    cv2.imwrite(f'nova_imagem{i}.png',nova_img)

    #mostrando as imagens com esteganografia
    print(f'Imagem com a ESTEGANOGRAFIA{i}:')
    cv2_imshow(nova_img)

esteganografia()

#Mostrando a imagens que estão dentro das outras
def extrair():
  for i in range(1,4):
    img = cv2.imread(f'/content/drive/MyDrive/Esteganografia/nova_imagem{i}.png')
    print(f'Imagem com a ESTEGANOGRAFIA{i}: ')
    cv2_imshow(img)
    extrair_img = img << 4
    print(f'Imagem EXTRAÍDA{i}:')
    cv2_imshow(extrair_img)

extrair()