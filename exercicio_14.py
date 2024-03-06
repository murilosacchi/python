far = float(input('Digite a temperatura da água em Fahrenheit '))
cel = (far-32)*(5/9)

if cel<0:
    print(f'O estado da água a {cel:.1f}ºC é sólido')

elif cel>0 and cel<100:
    print(f'O estado da água a {cel:.1f}ºC é líquido')

else:
    print(f'A temperatura da água a {cel:.1f}ºC é gasoso')