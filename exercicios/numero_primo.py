num_ok = False

while not num_ok:
    try:
        num = int(input('digite um número: '))
        if num >= 0:
            num_ok = True
        else:
            print('o número deve ser positivo')
    except:
        print('o número deve ser inteiro')

for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        print('o número não é primo')
        break
    else:
        print('o número é primo')
        break