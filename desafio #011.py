"""
desafio #011
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2mt^2
"""

alt=float(input("Digite a altura da parede:"))
lar=float(input("Digite a largura da parede:"))
area=(alt * lar)
print("A área da parede é {}.\nSerá necessário {} litros de tinta para pintura.".format(area,(area/2)))