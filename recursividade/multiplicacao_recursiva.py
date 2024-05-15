# Multiplicação Recursiva (x, y são >= 0)
def mult_rec(x, y):
  if y == 1:
    return x
  else:
    return x + mult_rec(x, y-1)

# Testes
print('-- Multiplicação recursiva --')
print(mult_rec(4, 6))
print(mult_rec(5, 1))
print(mult_rec(0, 456))