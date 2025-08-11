x = int(input('Digite um número '))
y = int(input('Digite outro número '))
z = int(input('Digite outro número '))
codigo = str(input('Digite o código de condição '))
lista = [x,y,z]

if codigo == 'c':
    lista_ordenada = sorted(lista)
    print(lista_ordenada)

elif codigo == 'd': 
    lista_ordenada = sorted(lista, reverse=True)
    print(lista_ordenada)

else:
    print('Código invalido')

