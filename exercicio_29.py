# Peça ao usuário para digitar um número dentro de um determinado intervalo (p. ex., entre 1 e 10). Use um while loop para continuar solicitando a entrada até que um valor válido seja fornecido. Em outras palavras, enquanto não for digitado um valor dentro desse intervalo, o programa continua solicitando a entrada do usuário.

num = int(input('Digite um valor entre 1 e 10: '))

while not 1 <= num <= 10:
    num = int(input('Digite um valor entre 1 e 10: '))
