"""
desafio #032
Faça um programa que leia um ano qualquer e mostre se ele é um ano bisexto.
"""

ano = int(input("Digite um ano: "))
if (ano % 4) == 0:
    print("O ano {} é um ano bisexto.".format(ano))
else:
    print("O ano {} não é um ano bisexto".format(ano))
