# Desafio 02
# Tranformar a lista em dicionário, sendo que:
# Cada chave é a palavra em letras minúsculas
# Cada valor é o número de caracteres da palavra, desconsiderando espaços em branco

# EXEMPLO RESULTADO:
# dict_caracteres = {
#     'olá' : 3,
#     'python' : 6,
#     'daniel' : 6,
#     'asimov academy' : 13
# }

palavras = ['Olá', 'Python', 'Daniel', 'Asimov Academy']

dict_caracteres = {
    palavra.lower() : len(palavra.replace(' ', ''))
    for palavra in palavras
}

print(dict_caracteres)