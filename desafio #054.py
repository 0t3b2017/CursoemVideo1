"""
desafio #054

Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas já são maiores (21 anos)
"""
from datetime import datetime

maior = 0
menor = 0

ano_nasc = int(input("Digite um ano de nascimento: "))
ano_atual = datetime.today().year
idade = ano_atual - ano_nasc

if idade >= 21:
    maior += 1
else:
    menor += 1


for i in range(1,7):
    ano_nasc = input("Digite outro ano de nascimento: ")

    if idade >= 21:
        maior += 1
    else:
        menor += 1

print("{} pessoas ainda não atigiram a maioridade.".format(menor))
print("{} pessoas já atigiram a maioridade.".format(maior))

