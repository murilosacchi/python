# Dada uma string, use um for loop para contar quantas vezes um determinado caractere aparece nela.

palavra = 'pneumoultramicroscopicossilicovulcanoconiótico'
contagem = 0 
caractere = 'a'

for letra in palavra:
    if letra == caractere:
        contagem += 1

print(f'A letra {caractere} aperece {contagem} vezes na string {palavra}')