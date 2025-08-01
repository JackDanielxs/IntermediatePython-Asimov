# Desafio 02
# Crie uma função chamada multiplicar_por. O que esta função faz é retornar uma nova função
# f capaz de multiplicar um número qualquer pelo fator n passado à função multiplicar_por.
#
# Exemplo de uso:
# dobrar = multiplicar_por(2)
# print(dobrar(3))       # output: 6
# print(dobrar(10))      # output: 20
# vezes_cinco = multiplicar_por(5)
# print(vezes_cinco(3))  # output: 15
# print(vezes_cinco(10)) # output: 50

def multiplicar_por(n):
    return lambda x: x * n

# Testes
dobrar = multiplicar_por(2)
print(dobrar(3))       # 6
print(dobrar(10))      # 20

vezes_cinco = multiplicar_por(5)
print(vezes_cinco(3))  # 15
print(vezes_cinco(10)) # 50