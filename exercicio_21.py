codigo = int(input('Digite o código do produto: '))
valor = float(input('Digite o valor do produto: '))

if codigo == 1:
    if valor > 1000:
        valorfinal = valor * 0.90
        print(f'O valor do produto com desconto é R${valorfinal:.2f}')
    else:
        print('Não há desconto')

elif codigo == 2:
    if valor > 100:
        valorfinal = valor * 0.95
        print(f'O valor do produto com desconto é R${valorfinal:.2f}')
    else:
        print('Não há desconto')

elif codigo == 3:
    if valor > 500:
        valorfinal = valor * 0.90
        print(f'O valor do produto com desconto é R${valorfinal:.2f}')
    else:
        print('Não há desconto')
        
else:
    print('Código inválido')