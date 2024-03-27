# Dada uma lista de números, use um for loop para verificar quais são números primos.

import random

lista_numeros = []
primos = []

for i in range(10):
    numero = random.randint(1, 100)
    lista_numeros.append(numero)
    for num in lista_numeros:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primos.append(num)

print(f'Números primos: {primos}')

        

