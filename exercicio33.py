# Dados dois números, use um while loop para encontrar o Mínimo Múltiplo Comum (MMC) entre eles.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

condicao = True

maior = max(num1, num2)

while condicao:
    if maior % num1 == 0 and maior % num2 == 0:
        condicao = False
    else:
        maior += 1

print(f"O MMC de {num1} e {num2} é {maior}.")
        