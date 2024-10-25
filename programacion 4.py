import random
estudiantesaux=""
estudiantes=[]
orden=[]
cant=0
rando=0

print("Ingrese la cantidad de estudiantes del curso")
cant=int(input())

for i in range(0,cant):
    print("Ingrese un alumno")
    estudiantesaux=input()
    estudiantes.append(estudiantesaux)
    
for i in range (len(estudiantes)):
    
    rando=random.randint(0,len(estudiantes)-1)
    ests=estudiantes[rando]
    orden.append(ests)
    del estudiantes[rando]
print (orden)
    

    

