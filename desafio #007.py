"""
desafio #007
Desenvolva um programa que leia duas notas de um aluno e mostre a média
"""

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = ((n1+n2)/2)
print("A média do aluno é: {:.1f}".format(media))
if media >= 6:
    print("Aluno aprovado! Congrats")
else:
    print("Aluno reprovado! I'm sorry...")