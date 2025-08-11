def entrada_notas():
    notas = []
    for i in range(1, 5+1):
        while True:
            try:
                nota = int(input(f'Digite a nota {i}: '))
                if 0 <= nota <= 100: 
                    notas.append(nota)
                    break
                else:
                    print('ERRO! A nota deve ser entre 0 a 100')
            except:
                print('ERRO! A nota deve ser um valor inteiro')
    return notas

def media(notas):
    media_notas = sum(notas) / len(notas)
    return media_notas

def conceito(media_notas):
    if media_notas < 60:
        conceito = 'F'
    elif 60 <= media_notas <= 69:
        conceito = 'D'
    elif 70 <= media_notas <= 79:
        conceito = 'C'
    elif 80 <= media_notas <= 89:
        conceito = 'B'
    else:
        conceito = 'A'
    return conceito

lista_notas = entrada_notas()
media_notas = media(lista_notas)
conceito_nota = conceito(media_notas)

print(f'Sua média é {media_notas} e o conceito é {conceito_nota}.')
