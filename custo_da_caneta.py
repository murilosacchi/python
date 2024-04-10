n = int(input('Quantas canetas foram compradas: '))
z = int(input('Quanto foi pago: '))
y = int(input('Quanto recebeu de troco: '))

custo = z - y
caneta = custo/n

print('O preço de cada caneta foi',f"{caneta:.2f}",'reais')