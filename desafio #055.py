"""
desafio #055
Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor pelo lidos.

"""

maior_peso = 0
menor_peso = 600

peso = int(input("Digite um peso: "))

if peso > maior_peso:
    maior_peso = peso

if peso < menor_peso:
    menor_peso = peso

for i in range(1, 5):
    peso = int(input("Digite outro peso: "))

    if peso > maior_peso:
        maior_peso = peso

    if peso < menor_peso:
        menor_peso = peso

print("O maior peso digitado foi {}.".format(maior_peso))
print("O menor peso digitado foi {}.".format(menor_peso))
