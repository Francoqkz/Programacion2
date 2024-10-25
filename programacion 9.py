import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageOps


im1= Image.open("Captura.png")
im1gr= ImageOps.grayscale(im1)
ar=np.array(im1gr)


filas=341
columnas=455

for i in range(filas):
    for j in range(int(columnas/2)):
        
        aux=ar[i][j]
        ind_op=columnas-1-j
        ar[i][j]=ar[i][ind_op]
        ar[i][ind_op]=aux


plt.imshow(ar, cmap='gray')
plt.show()