#Escribe un programa que tome una lista de números enteros como entrada del usuario. 
# Luego, convierte cada número en la lista a string y únelos en una sola cadena, 
# separados por guiones ('-'). Sin embargo, excluye cualquier número que sea múltiplo de 3 
# de la cadena final.


#creo una lista de numeros ingresados por teclado
ingreso_lista = input("Ingresá una lista de números separados por un espacio: ")
lista_numeros = ingreso_lista.split() 

#los uno separados por guiones e imprimo para verificar
lista_nueva = [elem for elem in lista_numeros if int(elem) %3 != 0]
nuevo_string = '-'.join(lista_nueva)
print(f'La lista final es: {nuevo_string}')
