dist = float(input('Digite a distância percorrida em Km: '))

if dist <= 5:
    tar = 5 + (4 * dist)

elif dist <= 10:
    tar = 5 + (5 * 4) + (3.5 * (dist - 5))

else:
    tar = 5 + (5 * 4) + (5 * 3.5) + (3 * (dist - 10))

print(f'O valor total da corrida é de R${tar:.2f}')
