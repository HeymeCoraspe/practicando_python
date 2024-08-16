#1 Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
'''
edad= int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")'''

#2 Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide
# con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
'''
contrasena_sistema= "olakease"

contrasena=input("Ingresa tu contraseña: ")

if contrasena_sistema == contrasena.lower():
    print("Contraseña válida")
else:
    print("Contraseña inválida")'''

#3 Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error.
'''
num1= int(input("Ingrese un número: "))
num2= int(input("Ingrese otro número: "))

if num1 == 0 or num2 == 0:
    print("No puedes dividir por cero")
else:
    operacion= num1/num2
    print(f'El resutado es de la división es: {operacion}')'''

#4 Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
'''
numero= int(input("Ingresa un número: "))

if numero%2 == 0:
    print("El número es par")
else:
    print("El número es impar")'''

#5 Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales.
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
'''
edad= int(input("Ingresa tu edad: "))
ingresos= float(input("Detalla el monto de tus ingresos: "))

def calculo_tributo():
    if edad >= 18 and ingresos >= 1000:
        print ("Debes abonar impestos")
    else:
        print("No abonas impuestos")

print(calculo_tributo())  '''

#6 Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A esta formado por las mujeres con un nombre anterior a la M (a a l) y los hombres con un nombre posterior a la N 
# y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, 
# y muestre por pantalla el grupo que le corresponde.
'''
sexo= input("Ingresa f o m según te corresponda: ").lower
nombre=input("Ingresa tu nombre: ").lower
 
if sexo == "M" and nombre < "M":
    grupo= "A"
else:
    grupo= "B"

print(f'Tu grupo es: {grupo}')'''

#7 Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
#Renta	Tipo impositivo Menos de 10000€	5% E     Entre 10000€ y 20000€	15%C     Entre 20000€ y 35000€	20%C
#Entre 35000€ y 60000€	30% B    Más de 60000€	45%A
#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
'''
cod_catA, cod_catB, cod_catC, cod_catD, cod_catE= "A","B", "C","D","E" 
impuesto_catA, impuesto_catB, impuesto_catC, impuesto_catD, impuesto_catE= 0.45, 0.30, 0.20, 0.15, 0.05

renta_anual= float(input("Ingrese el monto de su renta anual: "))

if renta_anual <= 10000:
    porcentaje= renta_anual*impuesto_catE
    total_renta=renta_anual + porcentaje
    print(f'Su categoria es {cod_catE}, el impuesto es de: {impuesto_catE}%') 
    print(f'El total a abonar es: ${total_renta}') 
elif renta_anual >10000 and renta_anual <= 20000:
    porcentaje= renta_anual*impuesto_catD
    total_renta=renta_anual + porcentaje
    print(f'Su categoria es {cod_catD}, el impuesto es de: {impuesto_catD}%') 
    print(f'El total a abonar es: ${total_renta}') 
elif renta_anual >20000 and renta_anual <= 35000:
    porcentaje= renta_anual*impuesto_catC
    total_renta=renta_anual + porcentaje
    print(f'Su categoria es {cod_catC}, el impuesto es de: {impuesto_catC}%') 
    print(f'El total a abonar es: ${total_renta}') 
elif renta_anual >35000 and renta_anual <= 60000:
    porcentaje= renta_anual*impuesto_catB
    total_renta=renta_anual + porcentaje
    print(f'Su categoria es {cod_catB}, el impuesto es de: {impuesto_catB}%') 
    print(f'El total a abonar es: ${total_renta}') 
elif renta_anual >60000 :
    porcentaje= renta_anual*impuesto_catA
    total_renta=renta_anual + porcentaje
    print(f'Su categoria es {cod_catA}, el impuesto es de: {impuesto_catA}%') 
    print(f'El total a abonar es: ${total_renta}') '''

#8 En una determinada empresa, sus empleados son evaluados al final de cada año. 
# Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. 
# Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. 
# A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. 
# La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel
#Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, 
# así como la cantidad de dinero que recibirá el usuario.
'''
puntos_catD, puntos_catC, puntos_catB, puntos_catA= 0.0, 0.4, 0.6, 1.5
nombre_cadD, nombre_cadC, nombre_cadB, nombre_cadA= "bajo", "medio", "alto", "premium" 
cantidad_dinero= 2400

categoria= input("Ingrese la categoría del empleado: ").lower()

if categoria == nombre_cadA:
    puntuacion= cantidad_dinero*puntos_catA
    total_dinero= cantidad_dinero+puntuacion
    print(f"La categoría del empleado es: {nombre_cadA} y el pago es de {total_dinero}")
elif categoria == nombre_cadB:
    puntuacion= cantidad_dinero*puntos_catB
    total_dinero= cantidad_dinero+puntuacion
    print(f"La categoría del empleado es: {nombre_cadB} y el pago es de {total_dinero}") 
elif categoria == nombre_cadC:
    puntuacion= cantidad_dinero*puntos_catC
    total_dinero= cantidad_dinero+puntuacion
    print(f"La categoría del empleado es: {nombre_cadC} y el pago es de {total_dinero}")    
elif categoria == nombre_cadD:
    puntuacion= cantidad_dinero*puntos_catD
    total_dinero= cantidad_dinero+puntuacion
    print(f"La categoría del empleado es: {nombre_cadD} y el pago es de {total_dinero}")   '''

#9 Escribir un programa para una empresa que tiene salas de juegos para todas las edades 
# y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€. 
'''
precio_hasta4= 0
precio_ninos= 5
precio_adulto= 10

edad= int(input("Ingrese la edad del cliente: "))

if edad < 4:
    print(f'El precio de la entrda es: ${precio_hasta4}, ¡entras gratis!')
elif edad >= 4 and edad < 18:
    print(f'El precio de la entrda es: ${precio_ninos}')
elif edad >= 18:
    print(f'El precio de la entrda es: ${precio_adulto}')    '''

#10 La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
# Los ingredientes para cada tipo de pizza aparecen a continuación.
#Ingredientes vegetarianos: Pimiento y tofu.        Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
# y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
#  Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
'''
pizza_veggie=["pimiento", "tofu"]
pizza_comun=["Peperoni", "Jamón", "Salmón"]

nombre=input("Ingresa tu nombre: ")
print(f'Bienvenido {nombre}, ¿Qué tipo de pizza quieres?')
tipo_pizza= int(input("Ingresa 1 para vegetariana o 2 para común: "))
print("*********************************************************")

if tipo_pizza== 1:
    print(f'Los ingredientes de tu pizza son: {pizza_veggie}')
    print("Tu compra viene con un extra de regalo, elige: ")
    extras=input(f'Ingresa m para muzzarella, t para tomate o h para huevo, n si no agregas nada: ').lower()
    print("************************************************************")
    if extras== "m":
        pizza_veggie.append("muzzarella")
        print(f'Tu pizza tendrá {pizza_veggie}')
    elif extras== "t":
        pizza_veggie.append("tomate")
        print(f'Tu pizza tendrá {pizza_veggie}')
    elif extras== "h":
        pizza_veggie.append("huevo")
        print(f'Tu pizza tendrá {pizza_veggie}')
    else:
        print(f'Tu pizza se mantiene igual: {pizza_veggie}')
    
if tipo_pizza== 2:
    print(f'Los ingredientes de tu pizza son: {pizza_comun}')
    print("Tu compra viene con un extra de regalo, elige: ")
    extras=input(f'Ingresa m para muzzarella, t para tomate o h para huevo, n si no agregas nada: ').lower()
    print("************************************************************")
    if extras== "m":
        pizza_comun.append("muzzarella")
        print(f'Tu pizza tendrá {pizza_comun}')
    elif extras== "t":
        pizza_comun.append("tomate")
        print(f'Tu pizza tendrá {pizza_comun}')
    elif extras== "h":
        pizza_comun.append("huevo")
        print(f'Tu pizza tendrá {pizza_comun}')
    else:
        print(f'Tu pizza se mantiene igual: {pizza_comun}') '''