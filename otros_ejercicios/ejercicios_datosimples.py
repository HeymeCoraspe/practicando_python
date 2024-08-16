#https://aprendeconalf.es/docencia/python/ejercicios/tipos-datos/
import math
#1 Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
'''
print("¡Hola Mundo!")'''

#2 Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
'''
saludo= "¡Hola Mundo de nuevo!"
print(saludo)'''

#3 Escribir un programa que pregunte el nombre del usuario en la consola
# después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!
# donde <nombre> es el nombre que el usuario haya introducido.
'''
nombre= input("Ingresa tu nombre: ")
print(f"¡Hola {nombre}!")   '''

#4Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética .
'''
import math
def calculo():
    resultado= math.pow((3+2)/(2*5), 2) #elevar(4,3) 4 al cubo
    return  resultado
print(calculo())'''

#5 Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
# Después debe mostrar por pantalla la paga que le corresponde.
'''
horas= float(input("Ingrese la cantidad de horas trabajadas en la semana: "))
precio_hora= float(input("Ingrese el valor de la hora: "))

def calcular_pago():
    total_pago= float(horas * precio_hora)

    return total_pago

print(calcular_pago())'''

#6 Escribir un programa que lea un entero positivo n, introducido por el usuario
# después muestre en pantalla la suma de todos los enteros desde 1 hasta n (suma=n(n+1)/2)
'''
numero= int(input("Ingrse un número: "))

def calcular_suma_hastan():

    suma= (numero*(numero+1))/2
    return int (suma)

print (calcular_suma_hastan())'''

#7 Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
# calcule el índice de masa corporal y lo almacene en una variable
#  y muestre por pantalla la frase Tu índice de masa corporal es <imc> 
# donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
'''
peso= int(input("Ingrese su peso en kg: "))
altura= float(input("Ingrese su altura en metro: "))

def indice_mc():
    imc= peso/math.pow(altura,2)
    imc_round= round(imc,2) #redondeo a los dígitos que se le pasen
    return imc_round

print(f"Tu índice de masa corporal es: {indice_mc()}")'''

#8 Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c>
#  y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y 
# <c> y <r> son el cociente y el resto de la división entera respectivamente.
'''
num1=int(input("Ingrese un número entero: "))
num2=int(input("Ingrese otro número entero: "))

def division_nums():
    if num1==0 or num2==0:
        print ("Cero no es un número válido para dividir")
    else:
        cociente= num1/num2
        resto= num1%num2
        return float(cociente), float(resto)
cociente, resto= division_nums() #se definen las variables afuera de la función para que puedan llamarse
print(f"El cociente es: {cociente} y el resto es: {resto}")'''

#9 Escribir un programa que pregunte al usuario una cantidad a invertir, 
# el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
'''
monto_inversion=float(input("Ingrese el monto que desea invertir: "))
porcentaje_interes= float(input("Ingrese el porcentaje anual %: "))
anios=int(input("Ingrese el número de años por lo que desea invertir: "))

def simular_plazofijo():
    interes_ganado= monto_inversion*(porcentaje_interes*anios/365)
    capital_recibido= monto_inversion + interes_ganado
    monto_total= round(capital_recibido, 2)
    return float(monto_total)

print(f"El monto que recibirá es de {simular_plazofijo()}")'''

#10Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
# Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete 
# así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
# Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos 
# en el último pedido y calcule el peso total del paquete que será enviado.
'''
cantidad_muñecas= int(input("Ingrese la cantidad de muñecas vendidas: "))
cantidad_payasos= int(input("Ingrese la cantidad de payasos vendidos: "))
peso_muñeca= 75; peso_payaso= 112

def calcular_peso_paquete():
    total_peso_muñecas= cantidad_muñecas*peso_muñeca
    total_peso_payasos= cantidad_payasos*peso_payaso
    total_peso_paquete= (total_peso_muñecas+total_peso_payasos)/1000

    return total_peso_paquete
print(f"Para {cantidad_muñecas} muñecas y {cantidad_payasos} payasos, el peso es de {calcular_peso_paquete()} Kg")'''

#11 Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros.
# Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros,introducida por el usuario. 
# Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. 
# Redondear cada cantidad a dos decimales.
'''
interes_anual= 0.04
dinero_depositado= float(input("Ingrese el monto a depositar: "))

def ahorros_anuales():
    interes_anio1=(dinero_depositado*interes_anual)
    ahorros_anio1= interes_anio1+dinero_depositado
    ahorros_anio2= (ahorros_anio1*interes_anual)+ahorros_anio1
    ahorros_anio3= (ahorros_anio2*interes_anual)+ahorros_anio2
    return  ahorros_anio1,  ahorros_anio2,  ahorros_anio3
    
ahorros_anio1, ahorros_anio2,ahorros_anio3=ahorros_anuales()

print(f"Total balance primer año: {round(ahorros_anio1)}")
print(f"Total balance segundo año: {round(ahorros_anio2)}")
print(f"Total balance tercer año: {round (ahorros_anio3)}")'''

#12 Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
# Después el programa debe mostrar el precio habitual de una barra de pan, 
# el descuento que se le hace por no ser fresca y el coste final total.
'''
precio_barra= 3.49
dcto_pan_viejo= 60
panes_viejos= int(input("Ingrese la cantidad de barras de ayer vendidas: "))

def calcular_dcto():
    dcto_por_barra= (precio_barra*dcto_pan_viejo)/100
    dcto_total= panes_viejos*dcto_por_barra
    total_panes= panes_viejos*precio_barra
    perdida= total_panes - dcto_total
    return dcto_por_barra, total_panes, perdida,dcto_total

dcto_por_barra, total_panes, perdida,dcto_total= calcular_dcto()
print(f"Precio normal del pan $: {precio_barra}")
print(f"Venta sin descuento $: {total_panes}")
print(f"Precio con descuento $: {dcto_por_barra}")
print(f"Total con descuento $: {round(dcto_total,2)}")
print(f"La pérdida es de $: {round(perdida,2)}")'''