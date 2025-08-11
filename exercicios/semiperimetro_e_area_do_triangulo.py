a = int(input('Insira o tamanho do lado A: '))
b = int(input('Insira o tamanho do lado B: '))
c = int(input('Insira o tamanho do lado C: '))

s=(a+b+c)/2
k=(s*(s-a)*(s-b)*(s-c))**0.5

print("O semiperímetro é", s)
print("A área é", f"{k:.2f}")