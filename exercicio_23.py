a = float(input('Digite o comprimento da linha A: '))
b = float(input('Digite o comprimento da linha B: '))
c = float(input('Digite o comprimento da linha C: '))

if a < b + c and b < c + a and c < a + b:
    if a == b == c:
        print('Esse triângulo é equilátero')
    
    elif a == b or a == c or b == c:
        print('Esse triângulo é isósceles')

    else:
        print('Esse triângulo é escaleno')

else: 
    print('Não é possível formar um triângulo com essas medidas')