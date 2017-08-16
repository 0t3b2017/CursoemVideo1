"""
desafio #020
O mesmo progessor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""
from random import sample
a1=input("Digite o nome de um aluno: ")
a2=input("Digite o nome de outro aluno: ")
a3=input("Digite o nome de outro aluno: ")
a4=input("Digite o nome de outro aluno: ")

alunos=(a1,a2,a3,a4)

print("A ordem de apresentação é {}".format(sample(alunos,4)))