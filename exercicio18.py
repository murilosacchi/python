ano = int(input('Digite o ano em formato YYYY: '))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f'O ano {ano} não é bissexto')

    else:
        print(f'O ano {ano} é bissexto')
            
else: 
    print(f'O ano {ano} não é bissexto')