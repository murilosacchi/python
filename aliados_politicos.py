from random import *
from collections import *

num_votos = int(input('Digite o número de votos para ver a concordância entre os candidatos: '))

def gera_votos(num_votos):
    x = []
    for i in range(num_votos):
        x.append(randint(0, 1))
    return x

def concordancia(x, y):
    contador = 0
    for i in range(len(x)):
        if x[i] == y[i]:
            contador += 1
    print(f'Houve concordância em {contador} votos')
    return contador

lista_nomes = ['Lula', 'Bolsonaro', 'Alckmin']

def gera_ficha_votos(lista_nomes, num_votos):
    Ficha = namedtuple('Ficha', 'nome votacao')
    fichas = []
    for nome in lista_nomes:
        votacao = gera_votos(num_votos)
        ficha = Ficha(nome=nome, votacao=votacao)
        fichas.append(ficha)
    return fichas

def busca_aliados(minha_ficha, fichas):
    