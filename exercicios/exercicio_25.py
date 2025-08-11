from math import *

a = float(input('Digite o comprimento do 1º lado: '))
b = float(input('Digite o comprimento do 2º lado: '))
c = float(input('Digite o comprimento do 3º lado: '))
s = (a + b + c) / 2
K = sqrt(s*(s-a)*(s-b)*(s-c))
print(f'a área do triângulo é {K:.2f}')