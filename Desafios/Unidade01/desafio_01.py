# Desafio 01
# Converta o loop abaixo para uma compreensão de lista

# for valor in valores:
#     triplo = valor * 3
#     triplos.append(triplo)

valores = [30, 50, 100, 120]
triplos = [valor * 3 for valor in valores]
print(triplos)
