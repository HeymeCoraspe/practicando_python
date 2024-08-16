#Introducir los lados de un triángulo y visualizar por pantalla si dicho triángulo es:
# equilátero:Tienen 3 lados iguales // isósceles: tienen dos lados iguales o escaleno:Todos sus lados son desiguales.
'''
lado_a=int(input("Introduzca el valor del lado A: "))
lado_b=int(input("Introduzca el valor del lado B: "))
lado_c=int(input("Introduzca el valor del lado C: "))

if lado_a == lado_b and lado_a == lado_c:
    print ("Es un triándulo equilátero")
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    print("Es un triángulo isósceles")
else:
    print("Es un tríangulo escaleno")     '''

#Realice un programa que le permita al usuario simular el pago ingresando el importe y la forma de pago:
#Contado (1): se aplica un descuento del 10% al importe
#Tarjeta (2): se aplica un interés de 10%
#Débito (3): se aplica un descuento del 5%
#Mostrar el importe, el descuento o interés y el importe total.
'''
forma_pago=int(input("Ingrese 1 para pago en efectivo, 2 para tarjeta de crédito o 3 para tarjeta de débito: "))
importe=float(input("Ingrese el monto a pagar: "))

if forma_pago == 1:
    total_efectivo = importe - (importe*0.10)
    print (f"Tiene un descuento del 10%, el monto a pagar es {total_efectivo}")
elif forma_pago == 2:
    total_tc= importe + (importe)* 0.10
    print (f"Tiene un recargo de 10%, el monto a pagar es {total_tc}")
elif forma_pago == 3:
    total_deb= importe - (importe*0.05)
    print (f"Tiene un descuento de 5%, el monto a pagar es {total_deb}")'''

#Realice un programa que lea tres números, muestre cuál es el mayor y determine si es par o impar.
'''
num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el segundo número: "))
num3=int(input("Ingrese el tercer número: "))

if num1>num2 and num1>num3:
    print (f"{num1} es el mayor")
    if num1%2==0:
        print(f"y es par")
    else:
        print("y es impar")   

elif num2>num1 and num2>num3:
    print (f"{num2} es el mayor")
    if num2%2==0:
        print(f"y es par")
    else:
        print("y es impar") 

elif num3>num1 and num3>num2:
    print (f"{num3} es el mayor")
    if num3%2==0:
        print(f"y es par")
    else:
        print("y es impar") '''

#Confeccione un programa que pida un número del 1 al 7 y diga el día de la semana correspondiente.
'''
print("¿Qué día es hoy?")
num_dia= int(input("Ingrese un número entre 1 y 7: "))

if num_dia == 1:
    print("¡Es Lunes!")
elif num_dia == 2:
    print("¡Es Martes!")
elif num_dia == 3:
    print("¡Es Miércoles!")
elif num_dia == 4:
    print("¡Es Jueves!")
elif num_dia == 5:
    print("¡Es Viernes!")
elif num_dia == 6:
    print("¡Es Sábado!")
elif num_dia == 7:
    print("¡Es Domingo!")'''

#Realice un programa que pida un número del 1 al 12 y diga el nombre del mes correspondiente.
'''
print("¿En qué mes estamos?")
num_mes= int(input("Ingrese un número entre 1 y 12: "))

if num_mes == 1:
    print("¡Estamos en Enero!")
elif num_mes == 2:
    print("¡Estamos en Febrero!")
elif num_mes == 3:
    print("¡Estamos en Marzo!")
elif num_mes == 4:
    print("¡Estamos en Abril!")
elif num_mes == 5:
    print("¡Estamos en Mayo!")
elif num_mes == 6:
    print("¡Estamos en Junio!")
elif num_mes == 7:
    print("¡Estamos en Julio!")
elif num_mes == 8:
    print("¡Estamos en Agosto!")
elif num_mes == 9:
    print("¡Estamos en Septiembre!")
elif num_mes == 10:
    print("¡Estamos en Octubre!")
elif num_mes == 11:
    print("¡Estamos en Noviembre!")
elif num_mes == 12:
    print("¡Estamos en Diciembre!")'''