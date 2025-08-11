#Uma biblioteca distribui um cartão magnético para que os alunos possam frequentá-la. A senha inicial, enviada pelo correio, é gerada automaticamente a partir da data de nascimento do aluno ('dd/mm/aaaa') do seguinte modo:

# mm'$'dd(invertido) + '#' + dd'!'mm(invertido) + '\'+aaaa

# Assim, se a data de nascimento é 25/10/1995, a senha será:

#10$52#25!01\1995

#Escreva um programa modular que solicite ao usuário a inserção da data de nascimento no formato dd/mm/aaaa e retorne sua senha de acordo com as regras da biblioteca.

nascimento = input('Digite a data de nascimento (dd/mm/aaaa): ')

def senha(nascimento):
    partes = nascimento.split("/")
    mes = partes[1]
    mes_invertido = mes[::-1]
    dia = partes[0]
    dia_invertido = dia[::-1]
    ano = partes[2]
    print(f'{mes_invertido}${dia_invertido}#{dia}!{mes}\{ano}')
    return dia, mes, ano, dia_invertido, mes_invertido

senha(nascimento)