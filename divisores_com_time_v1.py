# Escreva um programa em Python que exiba todos os divisores de um número inteiro fornecido pelo usuário. A versão anterior faz testes excessivos. Note que não é necessário testar todos os inteiros entre 1 e o inteiro fornecido pelo usuário... Basta testar até a metade do inteiro fornecido!

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

for i in range(1, num + 1):
    if num % i == 0:
        lista.append(i)

lista.sort(reverse=True)

print(lista)

fim = time()

tempo = fim - inicio
print(f'Tempo de processamento: {tempo:.2f} segundos')