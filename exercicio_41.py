# Elabore um programa Python que exiba todos os números pares entre zero e um número N fornecido pelo usuário. Requisito: Certifique-se de que o usuário tenha digitado um número positivo, inteiro ou real. Pense em qual caso engloba o outro!

ok = True

while ok:
    N = int(input('Digite um número positivo: '))
    if N > 0:
        ok = False
    else:
        print('ERRO: o número digitado deve ser positivo')

print(f'Os números pares entre 0 e {N} é: ')

for i in range(0, N, 2):
    print(i)




