# Elabore um programa modular que leia o nome do usuário e o imprima na vertical, em forma de escada, usando apenas letras maiúsculas.

nome = input('Digite o nome: ')

def nome_vertical(nome):
    nome = nome.upper()
    for i in range(1, len(nome) + 1):
        print(nome[:i])

nome_vertical(nome)