#Desafío 1 calcular el iva
#ingresar un precio.
#calcular el iva.
#mostrar precio final.

#precio_sin_iva= float(input("Ingrese el precio:"));
#calculo_iva= precio_sin_iva* 0.21 + precio_sin_iva;
#print("El precio con IVA es:", calculo_iva);

#############################################
#Desafío 2 calcular el iva
#ingresar un precio.
#ingresar el monto iva
#calcular el iva.
#mostrar precio final.

#precio_sin_iva= float(input("Ingrese el precio: "));
#monto_iva= float(input("Ingrese el monto del IVA: "));
#calculo_iva= (precio_sin_iva* monto_iva) + precio_sin_iva;
#print("El precio con IVA es:", calculo_iva);

#############################################
#Desafío 3
#ingrese monto en pesos
#calcular el equivalente en dóles
#mostrar en pantalla

#############################################
#pesos= int(input("Ingrese el monto en pesos: "));
#dolar= 1020;
#calculo_dolar= int(pesos / dolar);
#print("El monto en dólares es: US$",calculo_dolar);

#############################################
#Desafío 4
#crear una lista de 5 números al azar entre 0 y 9 ordenados y no repetidos
import random;

listado_random=[];

numero=random.randint(0,9);

while len(listado_random)<5:
    if numero not in listado_random: #para que no se repota ningún número
        listado_random.append(numero);#agregar el número en la lista si se cumple el if
    numero=random.randint(0,9);#creoando el número al azar para ir agregando hasta que se cumpla el while

listado_random.sort();

print(listado_random);






