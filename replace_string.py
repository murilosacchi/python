#  Construa um programa em Python que troque todas as ocorrencias de uma letra L1 pela letra L2 em uma string. A string e as letras L1 e L2 devem ser fornecidas pelo usuario.

string = input('Digite uma string: ')
l1 = input('Digite L1: ')
l2 = input('Digite L2: ')

def troca_string(string, l1, l2):
    novo_texto = string.replace(l1, l2)
    return novo_texto

texto_modificado = troca_string(string, l1, l2)

print(texto_modificado)
