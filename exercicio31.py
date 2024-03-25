#Suponha que uma população de organismos cresce exponencialmente a uma certa taxa por período. Use um while loop para simular o crescimento populacional até que ela atinja um limite desejado.

import math

populacao = 2000
taxa = 1.02
limite = 100000
periodo = 0

while populacao < limite:
    populacao = populacao * math.exp(taxa)
    periodo += 1
    print(f'{periodo} {populacao:.2f}')