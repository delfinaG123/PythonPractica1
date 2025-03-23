#Cree un programa que dada una lista de números imprima sólo los que son pares. 
# Nota: utilice la sentencia continue donde haga falta.
import random

#creo una lista de numeros random
lista_numeros = []
for i in range (random.randrange(2,10)):
    numeros_random = random.randrange(1,100)
    lista_numeros.append(numeros_random)

#Elijo cuales imprimir
for elem in lista_numeros:
    if (elem % 2 == 0):
        print(elem)
