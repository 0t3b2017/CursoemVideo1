"""
desafio #017
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
retângulo, calcule e mostre o comprimento da hipotenusa.
"""

# Forma matemática (A soma dos quadrados do cateto é igual a porra da hipotenusa)
#""""
c1=float(input("Digite o cateto oposto: "))
c2=float(input("Digite o cateto adjacente: "))
print("O comprimento da hipotenusa é {}.".format(((c1**2)+(c2**2))**(1/2)))
#"""

#"""
# Usando módulo
from math import hypot
#c1=float(input("Digite o cateto oposto: "))
#c2=float(input("Digite o cateto adjacente: "))
print("O comprimento da hipotenusa é {}.".format(hypot(c1,c2)))
#"""




