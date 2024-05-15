# Potência recursiva
def potencia(x, y):
    if y == 0:
        return 1
    else:
        return x * potencia(x, y-1)

# Testes
print('-- Potência recursiva --')
print(potencia(3, 0))
print(potencia(5, 3))
print(potencia(3, 4))