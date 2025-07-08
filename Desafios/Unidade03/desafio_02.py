# Desafio 02
# Crie um dicionário combos. Cada chave é uma tupla (comida, bebida) e o valor é a soma da combinação

import itertools

combo = {}

comidas = {
    'Prato Feito': 24.90,
    'Salada': 21.90,
    'Strogonoff': 29.90,
    'Feijoada': 32.90,
}

bebidas = {
    'Água': 3.90,
    'Refrigerante': 5.90,
    'Suco': 7.90,
}

# for chave_comida, preco_comida in comidas.items():
#     for chave_bebida, preco_bebida in bebidas.items():
#         chave_combo = (chave_comida, chave_bebida)
#         preco_combo = preco_comida + preco_bebida
#         combo[chave_combo] = round(preco_combo,2)


# for chave_combo in itertools.product(comidas, bebidas):
#     chave_comida, chave_bebida = chave_combo
#     preco_combo = comidas[chave_comida] + bebidas[chave_bebida]
#     combo[chave_combo] = round(preco_combo, 2)

for tupla in itertools.product(comidas.items(), bebidas.items()):
    chave_combo = tuple(tup[0] for tup in tupla)
    preco_combo = sum(tup[1] for tup in tupla)
    combo[chave_combo] = round(preco_combo, 2)
    
print(combo)