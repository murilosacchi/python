hor = int(input('Digite o número de horas trabalhadas: '))
val = float(input('Digite o valor recebido por hora: '))

val_adi = val*(0.5*(hor - 40))

if hor > 40:
  sal = (hor * val) + val_adi
  print(f'O salário a ser recebido é R${sal:.2f}')

else:
  sal = hor * val
  print(f'O salário a ser recebido é R${sal:.2f}')
