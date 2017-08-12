"""
# desafio #010
Crie um programa que leia quanto uma pessoa tem na carteira e mostre quandos dolares ela pode comprar.
Considere US$ 1.00 = R$ 3.27
"""
dolar=float(3.27)
reais=float(input("Quantos reais você tem? "))
print("Com R${} você pode comprar US${:.2f}!".format(reais,(reais / dolar)))