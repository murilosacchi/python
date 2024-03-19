conv = str(input('Digite o código de conversão (C ou F): '))

if conv == 'C':
  temp = float(input('Temperatura em graus Celsius: '))
  nova_temp = (temp * 9/5) + 32
  print(f'Conversão - Temperatura em graus Fahrenheit = {nova_temp:.2f}')

elif conv == 'F':
  temp = float(input('Temperatura em graus Fahrenheit: '))
  nova_temp = (temp - 32) * 5/9
  print(f'Conversão - Temperatura em graus Celsius = {nova_temp:.2f}')

else:
  print('Código inválido! Por favor, digite C ou F')