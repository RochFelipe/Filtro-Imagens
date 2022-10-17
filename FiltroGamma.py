
from PIL import Image
img = Image.open('imagens/pulmao.jpg')

matriz = img.load()

gamma = 0.6
for i in range(img.size[0]):
    for j in range(img.size[1]):
     r = int((matriz[i , j][0]/255) ** gamma * 255)
     g = int((matriz[i , j][1]/255) ** gamma * 255)
     b = int((matriz[i , j][2]/255) ** gamma * 255)
     matriz[i, j] = (r, g, b)

img.save('imagens/FiltroGammaAplicado.jpg')