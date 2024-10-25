import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["image.cmap"] = "plasma_r"

filas=50
columnas=50

matriz = [[0]*filas]*columnas
matriz = np.array(matriz)

for i in range(filas):
    for j in range(columnas):
        matriz[i][j]=i+j

print(matriz)
plt.imshow(matriz)

plt.show()

#matplotlib.image.imsave("fig2.png",matriz)