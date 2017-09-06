"""
desafio #035
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem
ou não formar um triânculo
"""

r1 = float(input("Digite o primeiro lado: "))
r2 = float(input("Digite o segundo lado: "))
r3 = float(input("Digite o terceiro lado: "))

if r1 > (r2 + r3):
    print("Não é possível formar um triângulo.")
elif r2 > (r1 + r3):
    print("Não é possível formar um triângulo.")
elif r3 > (r1 + r2):
    print("Não é possível formar um triângulo.")
else:
    print("É possível formar um triângulo.")