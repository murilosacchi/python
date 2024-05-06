# Escreva um programa que leia duas palavras e diga qual deles vem primeiro na ordem alfabetica. Dica: 'a' é menor do que 'b'.

palavra1 = input('Digite a primeira palavra: ')
palavra2 = input('Digite a segunda palavra: ')

def ordem_alfabetica(palavra1, palavra2):
    if palavra1 < palavra2: 
        print(f'a palavra {palavra1} vem primeiro que a {palavra2} em ordem alfabética')
    elif palavra2 < palavra1:
        print(f'a palavra {palavra2} vem primeiro que a {palavra1} em ordem alfabética')     
    else:
        print(f'as duas palavras começam com a mesma letra')

ordem_alfabetica(palavra1, palavra2)