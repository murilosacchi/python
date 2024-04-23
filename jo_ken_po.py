from random import *

def jogador():
    while True:
        jogada_jog = int(input('0 - Pedra\n1 - Papel\n2 - Tesoura\n\nDigite o número: '))
        if jogada_jog == 0 or jogada_jog == 1 or jogada_jog == 2:
            break 
        else:
            print('\nERRO! Digite somente o número correspondente\n')
    return jogada_jog

def computador():
    jogada_com = randint(0,2)
    return jogada_com

def quem_ganhou(jogada_jog, jogada_com):
    while True:
        if (jogada_jog == 0 and jogada_com == 2) or (jogada_com == 0 and jogada_jog == 2):
            return 'Pedra esmaga tesoura'
        elif (jogada_jog == 1 and jogada_com == 0) or (jogada_com == 1 and jogada_jog == 0):
            return 'Papel embrulha pedra'
        elif (jogada_jog == 2 and jogada_com == 1) or (jogada_com == 2 and jogada_jog == 1):
            return 'Tesoura corta papel'
        else:
            print('\nEmpate, jogue novamente\n')
        return quem_ganhou(jogador(), computador())

jogador1 = jogador()
jogador2 = computador()

while True:
    vencedor = quem_ganhou(jogador1, jogador2)
    print(f'\nResultado: {vencedor}')
    if vencedor != 'Empate':
        break


