"""
desafio #041

A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:

- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Junior
- Até 25 anos: Senior
- Acima: Master
"""

from datetime import date

ano_nasc = int(input("Digite o seu ano de nascimento com 4 dígitos: "))
ano_atual = date.today().year
idade = ano_atual - ano_nasc

print("O atleta tem {} anos.".format(idade))
if idade <= 9:
    print("Sua categoria é Mirim")
elif idade <= 14:
    print("Sua categoria é Infantil")
elif idade <= 19:
    print("Sua categoria é Junior")
elif idade <= 25:
    print("Sua categoria é Senior")
else:
    print("Sua categoria é Master")
