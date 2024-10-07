moedas = ['m25', 'm50', 'm100', 'b'] #entradas
estados = [0, 20, 50, 75, 100, 125, 150, 175, 200] 
estado_inicial = 0 #saldo inicial
estado_final = [200] #preco do refrigerante

#transição de estados
delta = {
    0:{'m25':(25,'n'),'m50':(50,'n'),'m100':(100,'n'),'b':(0,'n')},
    25:{'m25':(50,'n'),'m50':(75,'n'),'m100':(125,'n'),'b':(25,'n')},
    50:{'m25':(75,'n'),'m50':(100,'n'),'m100':(150,'n'),'b':(50,'n')},
    75:{'m25':(100,'n'),'m50':(125,'n'),'m100':(175,'n'),'b':(75,'n')},
    100:{'m25':(125,'n'),'m50':(150,'n'),'m100':(200,'n'),'b':(100,'n')},
    125:{'m25':(150,'n'),'m50':(175,'n'),'m100':(200,'n'),'b':(125,'n')},
    150:{'m25':(175,'n'),'m50':(200,'n'),'m100':(200,'t50'),'b':(150,'n')},
    175:{'m25':(200,'n'),'m50':(200,'t25'),'m100':(200,'t75'),'b':(175,'n')},
    200:{'m25':(200,'t25'),'m50':(200,'t50'),'m100':(200,'t100'),'b':(200,'r')}
}

#funcao que executa a maquina
def reconhecer(cadeia):
    estado = estado_inicial
    fim_cadeia = False
    i = 0
    saldo_total = 0
    try:
        while not fim_cadeia:
            if i == len(cadeia):
                fim_cadeia = True
            else:
                simbolo = cadeia[i]
                if simbolo in delta[estado]:
                    proximo_estado, troco = delta[estado][simbolo]
                    estado = proximo_estado
                    
                    if simbolo.startswith('m'):
                        valor = int(simbolo[1:])
                        saldo_total += valor 

                else:
                    raise ValueError  #simbolo fora das entradas
            i += 1
        if estado in estado_final:
            print('A cadeia ', cadeia, ' foi reconhecida')
            print(f'Troco: R${(saldo_total-200)/100:.2f}')
        else:
            print('A cadeia ', cadeia, ' foi rejeitada')
    except ValueError: 
        print('A cadeia ', cadeia, ' foi rejeitada')
    except Exception as e:
        print('Erro executando o autômato: ', e)

#testes
if __name__ == '__main__':
    reconhecer(['m100', 'm50', 'b']) #rejeita
    reconhecer(['m100', 'm100', 'm100', 'm25', 'b']) #aceita