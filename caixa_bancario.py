valor_ok = False

while not valor_ok:
    try:
        valor = int(input('Digite o valor a ser sacado: '))
        if valor % 2 == 0:
            valor_ok = True
        else:
            print('O valor deve ser par')
    except:
        print('o valor digitado não é inteiro')
        
notas100 = valor // 100
valor %= 100
notas50 = valor // 50
valor %= 50
notas20 = valor // 20
valor %= 20
notas10 = valor // 10
valor %= 10
notas5 = valor // 5
valor %= 5
notas2 = valor // 2
valor %= 2

print(f'Valor a ser sacado: {valor:.2f}')
print(f'Notas de 100: {notas100} nota')
print(f'Notas de 50: {notas50} nota')
print(f'Notas de 20: {notas20} nota')
print(f'Notas de 10: {notas10} nota')
print(f'Notas de 5: {notas5} nota')
print(f'Notas de 2: {notas2} nota')
        
            