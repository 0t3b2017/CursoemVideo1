"""
desafio #019
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um
programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
"""

from random import choice

alunos=["Lorena","Daysa","Paty","Beto"]
nome=choice(alunos)
print("O aluno escolhido para apagar o quadro é: {}.".format(nome))

