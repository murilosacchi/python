salario = float(input('Digite o seu sálario: '))
codigo = int(input('Digite o código do cargo:'))

if codigo == 310:
    salario_novo = salario*1.05
    diferenca = salario_novo-salario
    print(f'O seu salário atual de R${salario:.2f} terá um aumento de {diferenca:.2f} e você receberá {salario_novo:.2f}')
elif codigo == 410:
    salario_novo = salario*1.075    
    diferenca = salario_novo-salario
    print(f'O seu salário atual de R${salario:.2f} terá um aumento de {diferenca:.2f} e você receberá {salario_novo:.2f}')
elif codigo == 885:
    salario_novo = salario*1.1
    diferenca = salario_novo-salario
    print(f'O seu salário atual de R${salario:.2f} terá um aumento de {diferenca:.2f} e você receberá {salario_novo:.2f}')
else:
    salario_novo = salario*1.15
    diferenca = salario_novo-salario
    print(f'O seu salário atual de R${salario:.2f} terá um aumento de {diferenca:.2f} e você receberá {salario_novo:.2f}')
