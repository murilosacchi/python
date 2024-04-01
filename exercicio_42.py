""" Elabore um programa Python para gerenciar uma eleição. Os votos válidos são representados pelos números 1, 2 e 3, cada um correspondendo a um candidato. O voto em branco é representado pelo número 0 e o voto nulo, pelo número –1. O fluxograma deverá processar  𝑁  respostas da votação, calcular e exibir:

a) o total de votos para cada candidato;

b) o total de votos em branco;

c) o total de votos nulos;

d) a porcentagem de votos válidos do candidato vencedor.

Requisitos:

Use uma estrutura de repetição em conjunto com a função choice para gerar uma lista com os  𝑁  votos.
Use o método count para totalizar os votos. """

from random import choice 

ok = True
while ok:
    N = int(input('Digite o número de votos: '))
    if N > 0:
        ok = False
    else:
        print('ERRO: a votação deve ter pelo menos um voto')

escolhas = [-1, 0, 1, 2, 3]
votos = []
votos_validos = []

for i in range(N):
    votos.append(choice(escolhas)) 

candidato1 = votos.count(1)
candidato2 = votos.count(2)
candidato3 = votos.count(3)

print(f"O candidato 1 teve: {votos.count(1)} votos")
print(f"O candidato 2 teve: {votos.count(2)} votos")
print(f"O candidato 3 teve: {votos.count(3)} votos")
print(f"O total de votos em branco foi: {votos.count(0)} votos")
print(f"O total de votos nulos foi: {votos.count(-1)} votos")

votos_validos.append(candidato1)
votos_validos.append(candidato2)
votos_validos.append(candidato3)

campeao = votos_validos.index(max(votos_validos)) + 1
porcentagem = max(votos_validos)*100/(candidato1 + candidato2 + candidato3)

print(f"A porcetagem de votos válidos do candidato {campeao} é {porcentagem:.2f}%")










