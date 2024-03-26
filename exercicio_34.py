# Dada uma lista de notas de alunos, use um for loop para calcular a média das notas.

notas = (10, 1.3, 8.8, 3.5, 6, 4.5, 7.8, 5.2, 9.1, 2.3)
soma = 0

for nota in notas:
    soma += nota

media = soma / len(notas)

print(f'A média das notas é {media:.1f}')