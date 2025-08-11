p1 = float(input('digite a nota p1: '))
p2 = float(input('digite a nota p2: '))
t1 = float(input('digite a nota t1: '))
t2 = float(input('digite a nota t2: '))
t3 = float(input('digite a nota t3: '))

mf = ((p1 + p2) / 2 + (0.4 * t1 + 0.4 * t2 + 0.2 * t3)) / 2

if mf >= 6:
    print(mf, ' aprovado')
    
else:
    print(mf, ' reprovado') 