d = {'M1' : [67,79,90,73,36], 'M2': [89,67,84], 'M3': [82,57] }

contador = 0

for v in d.values():
  contador += len(v)

print(f'Total de itens na lista: {contador}')