# conte o numero de vogais na frase 'um pouco mais sobre listas'

frase = 'um pouco mais sobre listas'
vogais = [letra for letra in frase if letra in 'aeiou']
print(len(vogais))