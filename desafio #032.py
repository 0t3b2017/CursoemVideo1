"""
desafio #032
Faça um programa que leia um ano qualquer e mostre se ele é um ano bisexto.
"""
from datetime import date

ano = int(input("Que ano você quer analisar? Coloque 0 para o ano atual: "))

if ano == 0:
    ano = date.today().year

"""
if (ano % 400) == 0:
    print("\033[34mO ano {} é um ano bisexto.\033[m".format(ano))
else:
    if (ano % 4) == 0 and (ano % 100) != 0:
        print("\033[34mO ano {} é um ano bisexto.\033[m".format(ano))
    else:
        print("\033[31mO ano {} não é um ano bisexto\033[m".format(ano))
"""

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("\033[34mO ano {} é um ano bisexto.\033[m".format(ano))
else:
    print("\033[31mO ano {} não é um ano bisexto\033[m".format(ano))
