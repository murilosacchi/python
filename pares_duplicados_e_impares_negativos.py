from random import *

numeros = []
pares = []
impares = []

for i in range(10 + 1):
    numeros.append(randint(0, 100))

for j in numeros:
    if j % 2 == 0:
        pares.append(j*2)
    else:
        impares.append(j*(-1))    

numeros.sort()
pares.sort()
impares.sort(reverse=True)

print(numeros)
print(f'Pares: {pares}')
print(f'Impares: {impares}')