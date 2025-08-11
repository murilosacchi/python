texto = 'murilo'

def conta_vogais(texto):
    contador = 0
    for char in texto:
        if char in 'aeiouAEIOU':
            contador += 1
    print(f'O texto possui {contador} vogais') 
    return contador

def conta_consoantes(texto):
    contador = 0
    for char in texto:
        if char not in 'aeiouAEIOU ':
            contador += 1
    print(f'O texto possui {contador} consoantes')
    return contador

texto = input(str('Digite uma frase: '))
conta_vogais(texto)
conta_consoantes(texto)

