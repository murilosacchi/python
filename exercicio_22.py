valor_passado = float(input('Digite o valor passado do medidor: '))
valor_atual = float(input('Digite o valor atual do medidor: '))
resultado = valor_atual - valor_passado 

if 0 <= resultado >= 100:
    conta = resultado * 0.50

elif resultado <= 200:
    conta = 50 + ((resultado - 100) * 1) 

elif resultado <= 300:
    conta = 150 + ((resultado - 200) * 1.5)

else:
    conta = 300 + ((resultado - 300) * 2)

print(f'O número de unidades consumidas é {resultado:.0f}, e o valor da conta R${conta:.2f}')


