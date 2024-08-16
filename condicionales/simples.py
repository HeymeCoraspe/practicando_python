import math
#1. Realice un programa que solicite dos letras ingresadas por el usuario y verifique si son iguales o no, mostrando un mensaje."""
"""
letra_1= (input("Ingrese una letra: ").upper())
letra_2= (input ("Ingrese otra letra: ").upper())


if letra_1 == letra_2:
    print("Las letras son iguales")
else:
    print("Las letras son distintas")"""

#2 Hacer un programa que permita decidir si dos palabras son iguales o diferentes. Mostrar mensaje por pantalla.
"""
frase1= input("Ingrese la primera palabra: ").upper()
frase2= input("Ingrese la segunda palabra: ").upper()

if frase1 == frase2:
    print("Las palabras son iguales")
else:
    print("Las palabras son distintas")"""

#3 Realizar un programa que permita ingresar “f” o “m” y determinar si vota
"""genero= input("Ingrese F o M según su género: ").upper()

if genero == "F":
    print("Vota en mesa femenina")

if genero =="M":
    print("Vota en mesa masculina")"""

# 4 Realice un programa que lea dos números y diga cuál es el mayor.
"""num1= int(input("Ingrese el primer número: "))
num2= int(input("Ingrese el segundo número: "))

if num1 > num2:
    print("El primer número ingresado es el mayor")
else:
    print("El segundo número ingresado es mayor")"""

# 5 Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo el cambio de dólares a pesos 
# y que sea el usuario quién decida qué tipo de cambio quiere, si de dólares a pesos o viceversa.
"""cambio_dolar_peso= int(input("Ingrese 1 si desea cambiar de peso a dólar o 2 si es dólar a peso: "))
monto=int(input("Ingrese el monto sin puntos ni comas: "))
dolar=1465

if cambio_dolar_peso == 1:
    conversion_peso= monto*dolar
    print(f"El monto en pesos es AR$: {conversion_peso} ")

if cambio_dolar_peso== 2:
    conversion_dolar= math.floor(monto/dolar)
    print(f"El monto en dólar es US$: {conversion_dolar} ")"""

#6 Realice un programa donde el usuario ingrese su edad. 
# Si es mayor de 16 años, muestre un mensaje diciendo “puede votar”, sino “no vota”.
edad= int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Puedes votar")
else:
    print("No puedes votar")