# Construa uma função DNA_complementar que recebe uma string que representa uma cadeia de DNA e gera a cadeia complementar. A entrada e saída de dados deve ser feita pelo programa principal.

dna = input('Digite uma cadeia de DNA: ')

def dna_complementar(dna):
    dna = dna.upper()
    dna_comp = ''
    for base in dna:
        if base == 'A':
            dna_comp += 'T'
        elif base == 'T':
            dna_comp += 'A'
        elif base == 'G':
            dna_comp += 'C'
        elif base == 'C':
            dna_comp += 'G'
    return dna_comp

dna_comp = dna_complementar(dna)
print(dna_comp)

