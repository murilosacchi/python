# Escreva um programa que leia vários números reais em uma mesma linha, e imprima a soma.

numeros_str = input('Digite os números reais separados por espaço: ')

def soma_lista(numeros_str):
    numeros_separados = numeros_str.split()
    numeros = [float(numero) for numero in numeros_separados]
    soma = sum(numeros)
    print(f'A soma dos numeros {numeros} é {soma}')
    return numeros, soma

soma_lista(numeros_str)