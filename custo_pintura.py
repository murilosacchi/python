def entrada_dados():
    area = float(input('Digite a área a ser pintada: '))
    preco_galao = float(input('Digite o preço por galão da tinta escolhida: '))
    return area, preco_galao

area, preco_galao = entrada_dados()

def saida_dados():
    print(f'\nNúmero de galões de tinta necessário para o serviço: {num_galoes:.0f} galões')
    print(f'Quantidade de horas de trabalho previstas para a obra: {horas:.0f} horas')
    print(f'Custo relativo à tinta escolhida: {custo:.2f} reais')
    print(f'Taxa de mão de obra associada: {taxa:.2f} reais')
    print(f'Custo total da obra: {total:.2f} reais')



num_galoes = (area // 112) + 1
horas = num_galoes * 8 
custo = num_galoes * preco_galao
taxa = 35 * horas
total = custo + taxa

saida_dados()

