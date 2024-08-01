import random

rando=random.randint(1,20)
num=0
intentos=6
intentosR=0

while (intentosR<intentos):
    print("Intente adivinar el numero misterioso entren 1 y 20 / tiene ",intentos," vidas restantes")
    num=int(input())
    
    if num==rando:
        print("Felicidades, adivinaste el numero secreto con, " ,intentos,"vidas restantes")
        break
    else:
        if num>rando:
            
            intentos=intentos-1
            print("Numero equivocado, te quedan, ",intentos," vidas")
            print("El numero misterioso es menor que el ingresado por ud")
        else:
            intentos=intentos-1
            print("Numero equivocado, te quedan, ",intentos," vidas")
            
            if intentos>intentosR:
                print("El numero misterioso es mayor que el ingresado por ud")
            else:
                print("Te quedaste sin vidas, ahora esta computadora explotara :/")
                break