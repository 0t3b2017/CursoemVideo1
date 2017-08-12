"""
# desafio #009
Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
"""
num=int(input("Digite um número inteiro: "))
tab=int(1)
print("A tabuada de {} é:".format(num))
while tab <= 10:
    print("{} x {:<2} = {}".format(num, tab, (num*tab)))
    tab=tab+1