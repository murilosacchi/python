a = float(input('Digite o primeiro lado do triângulo '))
b = float(input('Digite o segundo lado  do triângulo '))
c = float(input('Digite o terceiro lado do triângulo '))

if a**2==(b**2)+(c**2):
    print('É um triângulo retângulo')

elif b**2==(c**2)+(a**2):
    print('É um triângulo retângulo')

elif c**2==(a**2)+(b**2):
    print('É um triângulo retângulo')

else:
    print('Não é um triângulo retângulo')