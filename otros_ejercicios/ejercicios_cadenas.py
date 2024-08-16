#1 Escribir un programa que pregunte el nombre del usuario en la consola y un número entero
# e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
'''
nombre= (input("Ingresa tu nombre: "))
numero= int(input("Ingresa un número: "))

for i in range(numero):

    print(f"Hola {nombre}!")'''

#2 Escribir un programa que pregunte el nombre completo del usuario en la consola
# después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, 
# otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
# El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
'''
nombre= (input("Ingresa tu nombre completo: "))

print(f"{nombre.lower()}")
print(f"{nombre.upper()}")
print(f"{nombre.title()}")'''

#3 Escribir un programa que pregunte el nombre del usuario en la consola
# después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras,
# donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
'''
nombre= (input("Ingresa tu nombre: "))
cantidad_letras=len(nombre)
print(f"Tu nombre {nombre.upper()} tiene {cantidad_letras} letras")'''

#4 Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension
# donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
# Escribir un programa que pregunte por un número de teléfono con este formato 
# y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
'''
num_telefono=(input("Ingrese el número con el siguiente formato prefijo-número-extension: "))

def convertir_telefono():
    telf= num_telefono[4:-3]
    return telf
print(F"El número es: {convertir_telefono()}")'''

#5 Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
'''
frase= input("Escriba una frase: ")

def invertir_frase():
    frase_invert= frase[::-1] #toma toda la cadena frase y la recorre de derecha a izquierda, creando una nueva cadena que es la versión invertida de la original.
    return frase_invert
print(invertir_frase())'''

# 6 Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, 
# y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
'''
frase= input("Escriba una frase: ")
vocal= input("Escriba una vocal: ")

def transformar_vocal():
    vocal_transform= frase.replace(vocal, vocal.upper()) #primero la vocal a reemplazar, segundo por lo que se va reemplazar
    return vocal_transform
print (transformar_vocal())'''

#7 Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico 
# con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
'''
email= input("Intruduce tu mail: ")

def reemplazar_dominio():
    email_reemplazo= email[:email.find("@")] + '@ceu.es' #encuentra el @
    return email_reemplazo
print(reemplazar_dominio())'''

#8 Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales
# y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
'''
def saludar(nombre, mensaje):
    print(f"Hola, {nombre}, {mensaje}")
if __name__ == "__main__":
    saludar(mensaje="Bienvenido", nombre="Juan")
    saludar(nombre="Juan", mensaje="Bienvenido")'''

#9Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
# Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
'''
fecha_nac= input("Introduce tu cumpleaños en formato dd/mm/aaaa: ")

def mostrar_fecha():
    dia=fecha_nac[:2]
    mes=fecha_nac[3:5]
    anio=fecha_nac[6:]
    return dia,mes,anio
dia,mes,anio=mostrar_fecha()
print(f"Día: {dia} Mes: {mes} Año: {anio}")'''
'''
fecha = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")
dia = fecha[:fecha.find('/')]
mesaño = fecha[fecha.find('/')+1:]
mes = mesaño[:mesaño.find('/')]
año = mesaño[mesaño.find('/')+1:]
print('Día', dia)
print('Mes', mes)
print('Año', año)'''

#10 Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas,
# y muestre por pantalla cada uno de los productos en una línea distinta.
'''
compras= input("Ingresa los productos que compraste separados por comas: ")

def mostrar_compras():
    lista= compras.replace(',','\n')
    return lista

print(mostrar_compras())'''

#11 Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y
#  muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, 
# el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
'''
nombre_producto= input ("Ingrese el nombre del producto: ")
precio_producto= float(input("Ingrese el precio por unidad: "))
cantidad_producto= int(input("Ingrese la cantidad del producto: "))

def calcular_monto():
    total_compra= precio_producto*cantidad_producto
    return total_compra

print (f'El total de su compra es: {calcular_monto()}')'''

