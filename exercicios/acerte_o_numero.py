import random
x = random.randint(1, 10)
chute = int(input('Tente acertar um número de 0 a 10: '))
while chute != x:
    print('Tente novamente :(')
    chute = int(input())
print('Você acertou!! ;)')