# Dada uma lista de números, use um for loop para verificar quais são números primos.

lista_numeros = range(2, 100)
primos = []

for num in lista_numeros:
    for i in range(2, num):
        if (num % i) == 0:
                break
    else:
        primos.append(num)

print(f'Números primos: {primos}')

        

