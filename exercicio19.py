idade = int(input('Digite sua idade: '))

if idade >= 0 and idade < 2:
    print('você é um bebê')

elif idade < 4:
    print('você é uma criança de colo')

elif idade < 13:
    print('Você é uma criança')

elif idade < 20:
    print('Você é um adolescente')

elif idade < 65:
    print('Você é um adulto')

elif idade < 100:
    print('Você é um idoso')

else:
    print('Idade inválida')

