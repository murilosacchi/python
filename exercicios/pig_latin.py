def pig_latin(frase):
    palavras = frase.split()
    nova_frase = []

    for palavra in palavras:
        nova_palavra = pig_latin_palavra(palavra)
        nova_frase.append(nova_palavra)

    return " ".join(nova_frase)

def pig_latin_palavra(palavra):
    primeira_letra = palavra[0]
    resto_da_palavra = palavra[1:]

    nova_palavra = resto_da_palavra + primeira_letra + "ay" 

    return nova_palavra

frase = str(input('Digita a frase a ser traduzida: '))
frase_traduzida = pig_latin(frase)

print(frase_traduzida)