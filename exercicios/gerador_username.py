nome = str(input('Digite seu nome: '))
sobrenome = str(input('Digite seu sobrenome: '))
RA = str(input('Digite seu RA: '))  

def gera_login(nome, sobrenome, RA):
    if len(nome) < 3:
        dnome = nome
    else:
        dnome = nome[:3]

    if len(sobrenome) < 3:
        dsobrenome = sobrenome
    else:
        dsobrenome = sobrenome[:3]

    if len(RA) < 3:
        dRa = RA
    else:
        dRA = RA[-3:]

    username = dnome+dsobrenome+dRA
    username = username.casefold()
    print(username)

        
gera_login(nome, sobrenome, RA) 
