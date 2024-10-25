import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["image.cmap"] = "plasma_r"

filas=40
columnas=40

matriz = [[0]*filas]*columnas
#matriz = np.array(matriz)

for i in range(filas):
    for j in range(columnas):
        matriz[i][j]=i+j

print(matriz[i][j])
#plt.imshow(matriz)

#plt.show()

#matplotlib.image.imsave("fig2.png",matriz)