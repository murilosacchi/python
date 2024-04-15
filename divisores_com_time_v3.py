# Escreva um programa em Python que exiba todos os divisores de um número inteiro fornecido pelo usuário. Também não é necessário testar todos os inteiros entre 1 e a metade do inteiro fornecido pelo usuário... É possível mostrar que basta testar até a raiz quadrada da entrada!

from time import *

num_ok = False

while not num_ok:
    try:
        num = int(input('Digite um número inteiro: '))
        if num > 0:
            num_ok = True
        else:
            print('ERRO! O número não é positivo')
    except:
        print('ERRO! O valor digitado não é inteiro')

inicio = time()

lista = []

for i in range(1, int(num**0.5) + 1):
    if num % i == 0:
        lista.append(i)
        if i != num // i:
            lista.append(num // i)

lista.sort(reverse=True)

print(lista)

fim = time()

tempo = fim - inicio
print(f'Tempo de processamento: {tempo:.2f} segundos')