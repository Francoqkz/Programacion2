import random

rando=random.randint(1,20)
num=0
intentos=6
intentosR=0
cantidad=20

def Dificultad2():
    rando=random.randint(1,200)
    num=0
    intentos=7
    intentosR=0
    cantidad=200
              
print("Hola! bienvenido, elija la dificultad en la que desea jugar: 2 para dificil o 1 para facil")
dificultad=int(input())

if dificultad==1:
    print("  ")
else:
    Dificultad2()
    
while (intentosR<intentos):
    print("Intente adivinar el numero misterioso entren 1 y ",cantidad," / tiene ",intentos," vidas restantes")
    num=int(input())
    
    if num==rando:
        print("Felicidades, adivinaste el numero secreto con, " ,intentos,"vidas restantes")
        break
    else:
        if num>rando:
            
            intentos=intentos-1
            print("Numero equivocado")
            print("El numero misterioso es menor que el ingresado por ud")
        else:
            intentos=intentos-1
            print("Numero equivocado")
            
            if intentos>intentosR:
                print("El numero misterioso es mayor que el ingresado por ud")
            else:
                print("Te quedaste sin vidas, ahora esta computadora explotara :/")
                break

    