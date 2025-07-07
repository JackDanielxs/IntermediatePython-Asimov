# Desafio 03

# Gostam de programação: Ricardo, Roberto, Pedro, Vinícius
# Gostam de futebol: Matheus, Roberto, Paulo, Vinícius
# Estudam na Asimov Academy: Ricardo, Matheus, Paulo, Pedro

# Usadno operações de conjunto, encontre o conjunto:
# Gostam de programação / Estudam na Asimov Academy / Não gostam de futebol

gostam_programacao = {'Ricardo', 'Roberto', 'Pedro', 'Vinícius'}
gostam_futebol = {'Matheus', 'Roberto', 'Paulo', 'Vinícius'}
estudam_asimov = {'Ricardo', 'Matheus', 'Paulo', 'Pedro'}

resultado = gostam_programacao | estudam_asimov
resultado -= gostam_futebol
print(resultado)