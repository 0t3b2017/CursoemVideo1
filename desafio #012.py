"""
desafio #012
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
"""

preco=float(input("Qual o preço original? R$ "))
desc=float(input("Qual o desconto a ser aplicado em porcentagem? "))
new_preco=(preco - ((preco * desc) / 100))
print("O valor com desconto de {}% é R$ {:.2f}".format(desc, new_preco))

