"""
desafio #051

Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos
dessa progressão.
"""

termo1 = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))

print("Em uma PA com o 1º termo sendo {} e a razão {}, os 10 primeiros termos são:".format(termo1, razao))
print(termo1)

for n in range(1,11):
    termo1 = termo1 + razao
    print(termo1)
