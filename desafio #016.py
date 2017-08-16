"""
desafio #016
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua posição inteira.
"""
from math import trunc
num=float(input("Digite um número real: "))
print("A parte inteira do número {} é {}.".format(num,trunc(num)))