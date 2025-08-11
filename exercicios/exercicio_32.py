# Simule o crescimento de um investimento ao longo do tempo com juros compostos. Use um while loop para calcular quanto tempo levará para o investimento dobrar.

montante = 1000
taxa = 0.1075
ano = 0
limite = 2 * montante

while montante <= limite:
    montante = montante * ((1 + taxa)**ano)
    ano += 1
    print(f'Ano {ano:.0f}: R${montante:.2f}')

print(f'O tempo para dobrar o invesimento: {ano:.0f} anos')