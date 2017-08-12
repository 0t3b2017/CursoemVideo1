"""
# desafio #008
Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
"""

metro=float(input("Digite um valor em metros: "))
print("{} metros equivale a {} centimetros e {} milimetros!".format(metro,(metro*100),(metro*1000)))