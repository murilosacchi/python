# Use um for loop para gerar os primeiros N termos da sequência de Fibonacci.

n = 10 
sequencia = [1, 1]

for i in range(2, n):
    sequencia.append(sequencia[i-1] + sequencia[i-2])

print(sequencia)


