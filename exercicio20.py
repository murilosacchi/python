caracter = input('Digite um único carácter: ')
decimal = ord(caracter)

if decimal >=65 and decimal <= 90:
    print('Letra maiúscula')

elif decimal >= 97 and decimal <= 122:
    print('Letra minúscula')

elif decimal >= 48 and decimal <= 57:
    print('Algarismo decimal')

elif decimal > 0 and decimal <= 255:
    print('Carácter especial')

else:
    print('Carácter inválido')