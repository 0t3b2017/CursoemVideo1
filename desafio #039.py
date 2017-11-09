"""
desafio #039

Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:

- Se ele ainda vai se alistar ao serviço militar;
- Se é a hora de se alistar;
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date
ano_nasc = int(input("Digite o ano de nascimento com 4 digitos: "))
ano_atual = date.today().year

while True:
    sexo = input("Digite seu sexo (F | M): ")
    if sexo in ["F", "f", "M", "m"]:
        break
    else:
        print("Sexo inválido, digite F ou M")

if sexo == "F" or sexo == "f":
    print("Pessoas do sexo feminino não precisam se alistar")

else:
    idade = ano_atual - ano_nasc
    if idade < 18:
        saldo = 18 - idade
        print("Você deve se alistar ao serviço militar em {}.".format(date.today().year + (18 - idade)))
        print("Ainda faltam {} anos.".format(saldo))
    elif idade == 18:
        print("Se você ainda não se alistou, corra. Você deve se alistar neste ano de {}.".format(date.today().year))
    else:
        saldo = idade - 18
        print("Se ainda não se alistou, ja está atrasado. Você deveria ter se alistado em {}.".format(int(date.today().year) - (idade - 18)))
        print("Ja se passaram {} anos.".format(saldo))
