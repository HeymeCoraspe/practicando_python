#1 Realice un programa que lea 4 números y diga cuántos son pares y cuantos impares y devuelva la sumatoria de los pares.
'''
i=0
pares=0
impares=0
num_ingresados=[]

for i in range (4):
    num= int(input("Ingrese un número: "))
    if num%2==0:
        pares= pares+1
        num_ingresados.append(num)
    else:
        impares= impares+1
        
print(f"La cantidad de números pares fue de: {pares}")
print(f"Los números impares fueron en total: {impares}")
print(f"La sumatoria de los números pares es: {sum(num_ingresados)}")'''

#Leer 10 números y obtener la cantidad de mayores y la cantidad de menores a 100, cuál es el número máximo y cuál es el número mínimo.
#.max()  .min() funciones para traer mayor/menor de la lista
'''
print("Ingresaremos 10 números en total")
lista_numeros=[]
i=0
mayores_100=0
menores_100=0

for i in range (10):
    num= int(input("Ingrese un número: "))
    if num >100:
        mayores_100 += 1
        lista_numeros.append(num)

    elif num<100:
        menores_100 +=1
        lista_numeros.append(num)
    
    num_max=max(lista_numeros)
    num_min=min(lista_numeros)

print(f"El número mayor es: {num_max}")
print(f"El número menor es: {num_min}")
print(f"La cantidad de mayores a 100 es: {mayores_100}")
print(f"La cantidad de menores a 100 es: {menores_100}")'''

#3 Ingresar las edades y el sexo de 15 personas determinar cuántas son mujeres, cuántos varones, cuántos mayores de edad y cuántos menores de edad.
'''
i=0; adult=0; child=0; female=0; male=0

for i in range (4):
    age= int(input("Ingrese edad: "))
    gender= int(input ("Ingrese 1 para fem y 2 para masc: "))
    if age >= 18:
        adult +=1
    elif age <18:    
        child += 1

    if gender == 1:
        female +=1
    elif gender == 2:
        male +=1

print(f"Hay {adult} adultos y {child} menores en total")
print(f"Hay {female} mujeres y {male} hombres en total")'''

#4 Leer 10 números y mostrar solamente los números positivos, y su sumatoria.
'''
i=0; positive_nums=0; positive_list=[]

for i in range (10):
    num= int(input("Ingrese un número (+ o -): "))

    if num > 0:
        positive_nums += 1
        positive_list.append(num)
        
print(f"Los números positivos ingresados fueron: {positive_list}")
print(f"La suma de los positivos es: {sum(positive_list)}")'''

#5 Leer 15 números negativos y convertirlos a positivos e imprimir dichos números.
'''
i=0; num=0; negative_list=[]; positive_list=[]

while i < 5:
    num= int(input("Ingrese un número negativo: "))
    i +=1
    negative_list.append(num)
for nums in negative_list:
    positive_list.append(nums*-1)
#pos= [nums *-1 for nums in negative_list]

print(positive_list)'''
