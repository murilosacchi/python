# Dada uma lista de nomes, use um for loop para formatar cada nome (por exemplo, capitalizando a primeira letra).

lista_nomes = ['murilo', 'RAMON', 'Enrico', 'arthur', 'MITCHEL']
nomes_formatados = []

for nome in lista_nomes:
    novo_formatado = nome.capitalize()
    nomes_formatados.append(novo_formatado)

print(nomes_formatados)