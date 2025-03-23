#Modifique el ejercicio 4 para que dada la lista de número genere dos nuevas
#listas, una con los número pares y otras con los que son impares. Imprima
#las listas al terminar de procesarlas.

import random

#creo una lista de numeros random
lista_numeros = []
for i in range (random.randrange(2,20)):
    numeros_random = random.randrange(1,100)
    lista_numeros.append(numeros_random)

#Los separo en dos listas
lista_pares = []
lista_impares = []
for elem in lista_numeros:
     lista_pares.append(elem) if (elem % 2 == 0) else lista_impares.append(elem)

#imprimo para comprobar
print('Imprimo lista de pares:')
for elem in lista_pares:
    print(elem, end=' ')
print('\nImprimo lista de impares:')
for elem in lista_impares:
    print(elem, end=' ')
