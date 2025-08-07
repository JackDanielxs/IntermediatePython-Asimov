# Crie uma função chamada ler_datas, que recebe um texto qualquer e
# extrai todas as datas que estejam escritas no formato DD/MM/AAAA
# como objetos datetime. Use o texto abaixo como exemplo

texto = """
A reunião está marcada para o dia 15/03/2023.
Lembre-se de entregar o relatório até 28/02/2023.
O evento acontecerá em 10/04/2023 no auditório principal.
"""

import re
import datetime

padrao = '[0-9]{2}/[0-9]{2}/[0-9]{4}'

datas = [
    datetime.datetime.strptime(datastr, '%d/%m/%Y')
    for datastr in re.findall(padrao, texto)
]

print(datas)