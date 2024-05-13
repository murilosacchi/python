dicionario = {
    1: "um",
    2: "dois",
    3: "três",
    4: "quatro",
    6: "seis",
    9: "nove",
    10: "dez"
}

d = {}

for key, value in dicionario.items():
  if key % 3 != 0:
    d[key] = value

print(d)