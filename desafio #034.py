"""
desafio #034
Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais,
o aumento é de 15%
"""

sal = float(input("Qual o seu salário?: R$ "))

if sal <= 1250.00:
    print("Seu salário será de R$ {:.2f}".format(sal+((sal*15)/100)))
else:
    print("Seu salário será de R$ {:.2f}".format(sal+((sal*10)/100)))
