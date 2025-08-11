qtd = int(input('Digite a quantidade que deseja comprar '))
val = qtd*100

if val>1000:
    dsct = val*0.9
    print(f'O custo total é de R${dsct:.2f}')
else:
    print(f'Você não tem direito ao desconto, portanto o custo total é R${val:.2f}')