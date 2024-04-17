from random import *

so = [1, 2, 3, 4, 5, 6]
x = randint(3000, 10000)
votos = choices(so, k = x)


windows = votos.count(1)
unix = votos.count(2)
linux = votos.count(3)
netware = votos.count(4)
macos = votos.count(5)
outro = votos.count(6)


print(f'Total de Votos: {len(votos)}\n')
print(f'Windows: {windows} ({(windows / len(votos))*100:.2f}%)\n')
print(f'Unix: {unix} ({(unix / len(votos))*100:.2f}%)\n')
print(f'Linux: {linux} ({(linux / len(votos))*100:.2f}%)\n')
print(f'Netware: {netware} ({(netware / len(votos))*100:.2f}%)\n')
print(f'Mac OS: {macos} ({(macos / len(votos))*100:.2f}%)\n')

sistemas = [windows, unix, linux, netware, macos, outro]
nome_sistemas = ['Windows', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']




