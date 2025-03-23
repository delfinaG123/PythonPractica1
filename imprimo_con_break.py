#Implementa un programa que solicite al usuario que ingrese una lista de números. 
# Luego, imprime la lista pero detén la impresión si encuentras un número negativo. 
# Nota: utilice la sentencia break cuando haga falta.

import random

lista_numeros = []
ingreso_lista = input("Ingresá una lista de números separados por un espacio: ")
for num in ingreso_lista.split():
    lista_numeros.append(int(num)) 

for elem in lista_numeros:
    if elem<0:
        break
    else:
        print (elem)
