import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageOps


im1= Image.open("Captura.png")
ar=np.array(im1)
g=np.zeros((341,455))

plt.imshow(ar, cmap='gray')
plt.show()

filas=341
columnas=455

for i in range(filas):
    for j in range(int(columnas)):
        g[i][j]=ar[i][j][0]*0.2989 + ar[i][j][1]*0.5870 + ar[i][j][2]*0.1140
        
        
plt.imshow(g, cmap='gray')
plt.show()
        
        

plt.imshow(ar)
plt.show()