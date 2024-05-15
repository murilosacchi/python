# Soma dos elementos de uma lista
def soma_lista(x):
    if not x:
        return 0
    else:
        return x[0] + soma_lista(x[1:])

# Testes
print('-- Soma recursiva de elementos em uma lista --')
print(soma_lista([]))
print(soma_lista([2]))
print(soma_lista([-5, 0, 4, 6]))
print(soma_lista([]))
print(soma_lista([2]))
print(soma_lista([-5, 0, 4, 6]))