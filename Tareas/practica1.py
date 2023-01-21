"""
1.Crea un programa que lea una lista de números del 
usuario (usando la función "input()") y los almacene en una lista.
"""

numeros=list(input('Ingrese una lista de números que desee: '))

print('Su lista de números es: ', numeros)

"""
2.Escribir una función que reciba como parámetro la lista de números
 y devuelva el promedio de los números de la lista.
"""
if numeros==0:
    valor_prom=0

valor_prom= len(numeros)
abecedario_int=list(map(int,numeros))

print('La cantidad de datos son: ', valor_prom)

prom= sum(abecedario_int)/valor_prom

print('El promedio de la lista es de: ',prom)