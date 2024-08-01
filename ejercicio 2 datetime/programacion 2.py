import datetime

fecha=datetime.date.today()
fechah=datetime.datetime.now()

print(fechah)
print(fecha)

a=int(input("Ingrese su año de nacimiento"))
m=int(input("Ingrese su mes de nacimiento"))
d=int(input("Ingrese su dia de nacimiento"))

nacimiento=0
nacimiento=date(a,m,d)

nacimiento=fecha-nacimiento

print(nacimiento)