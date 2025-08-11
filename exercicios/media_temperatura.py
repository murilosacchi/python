# A tabela a seguir, retirada de https://www.climatempo.com.br/climatologia/558/saopaulo-sp, registra as temperaturas mínimas e máximas típicas para cada mês do ano na capital paulista. Elabore um programa Python que, a partir das informações da tabela anterior, calcule e exiba a temperatura média para cada mês em São Paulo.

temp_min = [19, 19, 19, 17, 14, 13, 12, 13, 14, 16, 17, 18]
temp_max = [27, 28, 27, 25, 23, 22, 22, 23, 24, 25, 26, 26]
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
media = []

for i in range(len(temp_min)):
  media.append((temp_min[i] + temp_max[i])/2)

for j in range(len(meses)):
  print(f'{meses[j]}: {media[j]}')
