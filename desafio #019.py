"""
desafio #019
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um
programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
"""

from random import choice,sample

alunos=["Lorena","Daysa","Paty","Beto"]
nome=(str(sample(alunos,1)))
print("O aluno escolhido para apagar o quadro é: {}.".format(nome))

