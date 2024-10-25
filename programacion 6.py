Matriz=[[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]
contador=0
suma=0
suma2=0
csuma=0
multiplicacion=1
multiplicacion2=1
cmulti=1


for i in range(4):
    for j in range(4):
        contador=contador+1
        if (i==j):
            suma2=suma2+Matriz[i][j]
            multiplicacion2=multiplicacion2*Matriz[i][j]
            
        if(j==3-i):
            csuma=csuma+Matriz[i][j]
            cmulti=cmulti*Matriz[i][j]
            
        suma=suma+Matriz[i][j]
        multiplicacion=multiplicacion*Matriz[i][j]
        if contador>3:
            print(Matriz[i][j])
            contador=0
        else:
            print(Matriz[i][j],end="")
            print(",",end="")
            
print("     ")
print("La suma total de esta matriz es de :",suma)
print("La multiplicacion total de esta matriz es de :",multiplicacion)
print("La suma de la diagonal de esta matriz es de :",suma2)
print("La multiplicacion en diagonal de esta matriz es de :",multiplicacion2)
print("La suma de la contradiagonal de esta matriz es de :",csuma)
print("La multiplicacion en contradiagonal de esta matriz es de :",cmulti)


