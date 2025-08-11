# Elabore um programa modular para ordenar uma lista de títulos de livros em ordem alfabética e deixá-los separados por vírgula.

titulos = """O Senhor dos Anéis
Harry Potter e a Pedra Filosofal
1984
O Lobo da Estepe
Cem Anos de Solidão
A Metamorfose
A Revolução dos Bichos
Crime e Castigo
Macunaíma"""

def ordernar_titulos(titulos):
    lista_titulos = titulos.split('\n')
    lista_titulos.sort()
    return lista_titulos

def juntar_titulos(lista_titulos):
    titulos_separados_por_virgula = ', '.join(lista_titulos)
    print(titulos_separados_por_virgula)
    return titulos_separados_por_virgula

titulos_ordenados = ordernar_titulos(titulos)
juntar_titulos(titulos_ordenados)