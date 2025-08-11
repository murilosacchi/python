# O programa utiliza uma forma simplificada de juros compostos, em que os juros são calculados uma vez ao ano e adicionados ao valor investido. A saída do programa é um relatório em formato tabular que mostra, para cada ano do investimento, o saldo inicial, os juros ganhos no ano e o saldo final. Após a saída tabular, o programa imprime o valor total do saldo do investimento e o valor total de juros auferidos no período.

val = float(input('Digite o valor inicial a ser investido: '))
ano = int(input('Digite o período do investimento em anos: '))
jur = float(input('Digite a taxa de juros anual (em %): '))

total_juros = 0

for i in range(1, ano + 1):
    juros = (jur / 100) * val
    val += juros
    total_juros += juros 

print(f"Valor disponível ao final do período: {val:.2f} reais\nJuros auferidos no período: {total_juros:.2f} reais")