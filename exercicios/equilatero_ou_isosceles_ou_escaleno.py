a = int(input('Digite a medida do primeiro lado do triângulo '))
b = int(input('Digite a medida do segundo lado do triângulo '))
c = int(input('Digite a medida do terceiro lado do triângulo '))

if a==b==c:
    print('O triângulo é equilátero')

elif a==b!=c:
    print('O triângulo é isósceles')

elif b==c!=a:
    print('O triângulo é isósceles')

elif a==c!=b:
    print('O triângulo é isósceles')

else:
    print('O triângulo é escaleno')