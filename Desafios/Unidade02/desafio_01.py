# Desafio 01
# Crie uma função que retorna se um número inteiro é primo

def isPrimo(num):

    if num <= 2:
        return True
    
    for i in range(2, num):
        if(num % i == 0):
            return False
    
    return True