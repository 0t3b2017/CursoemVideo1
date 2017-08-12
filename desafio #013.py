"""
desafio #013
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
"""

sal=float(input("Qual o salário atual? R$ "))
aumento=float(input("Qual a porcentagem do aumento? "))
new_sal=(sal + (sal * aumento)/100)
print("O novo salário com {}% de aumento é R$ {:.2f}".format(aumento,new_sal))
