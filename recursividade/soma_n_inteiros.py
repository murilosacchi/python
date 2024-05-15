# Soma dos n primeiros inteiros
def soma_todos(n):
    if n == 0:
        return 0
    else:
        return n + soma_todos(n-1)

# Testes
print('-- Soma recursiva de todos os inteiros até n --')
print(soma_todos(1))
print(soma_todos(10))
print(soma_todos(50))