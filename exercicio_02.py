import math

V0 = int(input('Insira a velocidade inicial: '))
θ = int(input("Insira o angulo entre o cano do canhão e o solo: "))
g = 10

angulo_radiano = math.radians(2*θ)
seno = math.sin(angulo_radiano)

S = ((V0**2)/g)*seno

print("O alcance do projétil é de", f"{S:.2f}", "metros.")