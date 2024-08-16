#1- Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:
''' 
numero= input("Ingresa un número de tres dígitos: ")
numero_invertido= str(numero)[::-1] #convertir a string para poder usar slicing
print(f'El número invertido es {numero_invertido}')'''
'''
lista=[]
for i in range (3):
    num=int(input("Ingrese un número:"))
    lista.append(num)
    
lista_inver= lista.reverse()   

print(lista)'''

#2- Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, 
# que indique qué hora marcará el reloj dentro de h horas:
'''
t=int(input("Ingrese la hora en formato 24: "))
h=int(input("Ingrese hora conteo (hh): "))

calculo_hora= (t+h)%24
print(f'En {h} horas seran las {calculo_hora}:00')'''

#3 Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
'''
numero= int(input("Ingrese un número: "))

if numero%2==0:
    print("El número es primo")
else:
    print("El número no es primo")'''

#4 Tiempo de viaje. Un viajero desea saber cuánto tiempo tomó un viaje que realizó.
# Él tiene la duración en minutos de cada uno de los tramos del viaje.
#Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y
#entregue como resultado el tiempo total de viaje en formato horas:minutos.
#El programa deja de pedir tiempos de viaje cuando se ingresa un 0.

