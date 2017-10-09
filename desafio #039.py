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

idade = ano_atual - ano_nasc

if idade < 18:
    print("Você ainda deve se alistar ao serviço militar daqui à {} ano(s).".format(18 - idade))
elif idade == 18:
    print("Se você ainda não se alistou, corra. Você deve se alistar neste ano de {}.".format(date.today().year))
else:
    print("Se ainda não se alistou, ja está atrasado. Você deveria ter se alistado em {}.".format(int(date.today().year) - (idade - 18)))