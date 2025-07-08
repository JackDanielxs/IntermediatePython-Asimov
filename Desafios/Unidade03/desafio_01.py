# Desafio 01
# Crie uma função que retorna os valores de duas listas de forma intercalada
# Resultado = [1, 'a', 2, 'b', 3, 'c', 'd', 'e']

import itertools

L1 = [1, 2, 3]
L2 = ['a', 'b', 'c', 'd', 'e']

def intercalar(lista1, lista2):
    resultado = []
    for valor1, valor2 in itertools.zip_longest(lista1, lista2):
        if valor1 is not None:
            resultado.append(valor1)
        if valor2 is not None:
            resultado.append(valor2)
    return resultado

print(intercalar(L1, L2))