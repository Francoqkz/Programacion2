
print("Ingrese la palabra que desea cifrar :")
palabra=input()

print("Elija el numero de desplazamiento de su cifrado")
desplazamiento=int(input())

def cifradoCesar(palabra,desplazamiento):
    
    for i in palabra:
        cifrado=ord(i)+desplazamiento
        if(cifrado>ord("Z")):
            cifrado=cifrado-26
            
        if(cifrado>ord("A")):
            cifrado=cifrado+26
            
        texto=chr(cifrado)
        print(texto,end="")
        
    
print(cifradoCesar(palabra,desplazamiento))

print("¿Desea cifrar otra palabra? si/no")
desicion=input()

while desicion == "si":
    print("Ingrese una nueva palabra a cifrar")
    palabra=input()
    
    print("Elija el numero de desplazamiento de su cifrado")
    desplazamiento=int(input())
    
    print(cifradoCesar(palabra,desplazamiento))

    print("¿Desea cifrar otra palabra? si/no")
    desicion=input()



