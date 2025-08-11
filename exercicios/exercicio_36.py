# Dado um número, use um for loop para gerar a tabuada desse número até um determinado limite.

limite = 10
numero = 5

for i in range(1, limite+1):
    resultado = numero * i 
    print(f'{numero} x {i} = {resultado}')
