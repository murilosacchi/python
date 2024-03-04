import math   

a = float(input('Digite o número A: '))
b = float(input('Digite o número B: '))
c = float(input('Digite o número C: '))

if a>0:
    delta = math.sqrt(b**2-4*a*c)
    if delta>=0:
        raiz1 = (-b+delta)/2*a
        raiz2 = (-b-delta)/2*a
        print(f'as raízes da equação do 2º grau são {raiz1} e {raiz2}')
        
    else:
        print('Não é uma equação do 2º grau')
