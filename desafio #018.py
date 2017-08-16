"""
desafio #018
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse ângulo
"""
from math import sin,cos,tan,radians,ceil
angulo=(int(input("Digite um ângulo: ")))
rad=radians(angulo)
print("A seno do angulo {} é {:.3f}".format(angulo,sin(rad)))
print("A cosseno do angulo {} é {:.3f}".format(angulo,cos(rad)))
print("A tangente do angulo {} é {}".format(angulo,ceil(tan(rad))))