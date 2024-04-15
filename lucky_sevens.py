from random import *

dinheiro = int(input('Digite e quantia de dinheiro que deseja ter para apostar: '))
rodadas = 0
vitorias = 0
derrotas = 0

while dinheiro > 0:
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    soma_dados = dado1 + dado2
    print(f'o dado 1 deu {dado1} e o dado 2 deu {dado2}, resultando {soma_dados:.0f}')
    if soma_dados == 7:
        saldo = dinheiro + 4
        dinheiro = saldo
        print(f'Venceu! Você ganhou 4 reais e seu saldo é {saldo:.2f}')
        vitorias += 1
    else:
        saldo = dinheiro - 1
        dinheiro = saldo
        print(f'Perdeu! Você perdeu 1 real e seu saldo é {saldo:.2f}')
        derrotas += 1
        
    rodadas += 1
        
    while True:
        continuar_jogando = input('Dejesa continuar jogando? (sim / não): ')
        if continuar_jogando.lower() in ['sim', 'não']:
            break
        else:
            print('Resposta inválida. Digite sim ou não')
            
    if continuar_jogando.lower() == 'não':
        print(f'Obrigado por jogar\nVocê jogou {rodadas} rodadas\nSeu saldo é {dinheiro:.2f} reais\nVitórias: {vitorias}\nDerrotas: {derrotas}')
        break
    
if dinheiro == 0:
    print(f'Fim de jogo\nVocê jogou {rodadas} rodadas\nVitórias: {vitorias}\nDerrotas: {derrotas}')
    
        
        
    

    
        