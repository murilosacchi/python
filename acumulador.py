#Elabore um programa em Python que acumula a soma de uma sequência de números inteiros com início em um limite inferior e término em um limite superior, ambos fornecidos pelo usuário. O programa deve exibir também a sequência de números no formato de uma lista.

lim_ok = False

while not lim_ok:
    try:
        inf = int(input('Digite o limite inferior: '))
        sup = int(input('Digite o limite superior: '))
        if sup > inf:
            lim_ok = True
        else:
            print('ERRO! O limite superior deve ser maior que o limite inferior')
    except:
        print('ERRO! Os números devem ser inteiros')

soma = 0
lista = []

for i in range(inf, sup + 1):
    soma += i
    lista.append(i)

print(f'A soma dos números entre {inf} e {sup} é {soma:.0f}')
print(f'Os números somados são {lista}')
        