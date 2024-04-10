from math import *   

a = float(input('Digite o número A: '))
b = float(input('Digite o número B: '))
c = float(input('Digite o número C: '))

if a!=0:
    delta = (b**2-4*a*c)
    if delta>0:
        raiz1 = (-b+sqrt(delta))/2*a
        raiz2 = (-b-sqrt(delta))/2*a
        print(f'as raízes da equação do 2º grau são {raiz1} e {raiz2}')
    elif delta==0:
        raiz3 = (-b)/2*a
        print(f'a raíz da equação do 2º grau é {raiz3}')
    else:
        print('Não é uma equação do 2º grau')
else:
        print('Não é uma equação do 2º grau')
