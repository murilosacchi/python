# Inicialize uma lista com 20 números inteiros entre 0 e 200 e a imprima. Armazene os números pares em uma lista pares e os números ímpares em uma lista impares. Organize os valores das listas em ordem crescente e as imprima.

from random import *

numeros = []
pares = []
impares = []

for i in range(20):
  numeros.append(randint(0, 200))

for numero in numeros:
  if numero % 2 == 0:
    pares.append(numero)
  else:
    impares.append(numero)

pares.sort(reverse=True)
impares.sort(reverse=True)

print(f'Pares: {pares}')
print(f'Impares: {impares}')