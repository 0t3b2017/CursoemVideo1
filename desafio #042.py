"""
desafio #035
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem
ou não formar um triângulo

desafio #042
Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

- Equilátero - Todos os lados iguais.
- Isósceles - Dois lados iguais.
- Escaleno - Todos os lados diferentes.
"""

r1 = float(input("Digite o primeiro lado: "))
r2 = float(input("Digite o segundo lado: "))
r3 = float(input("Digite o terceiro lado: "))

if (r1 > (r2 + r3)) or (r2 > (r1 + r3)) or (r3 > (r1 + r2)):
    print("Não é possível formar um triângulo.")
else:
    print("É possível formar um triângulo.")
    if (r1 == r2) and (r1 == r3):
        print("Triângulo será Equilátero!")
    elif (r1 == r2) or (r1 == r3) or (r2 == r3):
        print("Triângulo será Isósceles!")
    else:
        print("Triângulo será Escaleno!")
