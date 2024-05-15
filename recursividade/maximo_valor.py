# Máximo valor em uma lista
def max_valor(x):
    if len(x) == 1:
        return x[0]
    else:
        max_resto = max_valor(x[1:])
        return max(x[0], max_resto)

# Testes
print('-- Máximo valor em uma lista [recursiva] --')
print(max_valor([-3, 4, 6, 90, 45]))
print(max_valor([-5]))
print(max_valor([-3, 4, 6, 90, 45]))
print(max_valor([-5]))
