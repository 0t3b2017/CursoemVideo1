"""
desafio #027
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e
o último nome separadamente.
"""

name = str(input("Digite seu nome: ")).strip().title()
dividido = name.split()
primeiro = dividido[0]
ultimo = dividido[len(dividido)-1]
print("Muito prazer em conhecê-lo {}.".format(name))
print("Seu primeiro nome é {}".format(primeiro))
print("Seu último nome é {}".format(ultimo))
print("Seu usuário é: {}.{}".format(primeiro, ultimo).lower())
