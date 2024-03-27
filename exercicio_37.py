# Dado um intervalo de números, use um for loop para calcular a soma dos números pares dentro desse intervalo.

num1 = 10
num2 = 20
soma = 0 
lista_pares = []

for i in range(num1, num2 + 1):
    if i % 2 == 0:
        lista_pares.append(i)
        soma += i

print(f'Os numeros pares são {lista_pares}. A soma dos números pares entre {num1} e {num2} é {soma}')