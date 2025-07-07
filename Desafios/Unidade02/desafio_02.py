# Desafio 02
# Tendo duas funções que simulam operações em banco de dados:
# busca_dados - retorna info 50% das vezes
# processa_dados - processa a info obtida

# Use os operadores e expressores para simplificar o bloco de código

import random

def busca_dados():
    if random.random() > 0.5:
        return None
    return 'teste'

def processa_dados(info):
    return f'Dados "{info}" foram processados'


result = (
    processa_dados(dados)
    if(dados := busca_dados()) is not None
    else 'N/A'
)
print(result)