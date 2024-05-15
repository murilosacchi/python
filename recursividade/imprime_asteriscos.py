# Imprime asteriscos com recursividade (n >= 0)
def imprime_asteriscos(n):
    if n > 1:
        imprime_asteriscos(n-1)
    print('*'*n)


# Testes
print('-- Impressão de asteriscos [recursivo] --')
imprime_asteriscos(10)
imprime_asteriscos(0)