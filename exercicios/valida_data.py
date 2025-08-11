def verifica_barras(data):
    partes = data.split("/")
    
    if len(partes) != 3:
        return False
    
    try:
        dia = int(partes[0])
        mes = int(partes[1])
        ano = int(partes[2])
    except ValueError:
        return False
    
    if not (1 <= dia <= 31):
        return False
    
    if not (1 <= mes <= 12):
        return False
    
    return True

def verifica_campos(data):
    
    if not verifica_barras(data):
        return False
    
    partes = data.split("/")

    try: 
        dia = int(partes[0])
        mes = int(partes[1])
        ano = int(partes[2])
    except ValueError:
        return False
    
    return dia, mes, ano

def main():
    while True:
        data = input('Digite a data no formato DD/MM/AAAA: ')

        campos = verifica_campos(data)

        if campos:
            dia, mes, ano = campos
            print(f'Dia: {dia}\nMês: {mes}\nAno: {ano}')
            break
        else:
            print('Data inválida. Tenta novamente.')

main()